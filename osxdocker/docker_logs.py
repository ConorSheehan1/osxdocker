import fire
import subprocess
import os


class DockerLogs:
    def __init__(
        self,
        screen_name="osxdocker",
        encoding="utf-8",
        vm_path="~/Library/Containers/com.docker.docker/Data/vms/0/tty",
    ):
        self.screen_name = screen_name
        self.encoding = encoding
        self.vm_path = vm_path

    def _get_shell_output(self, args):
        # subprocess stdout is in bytes with trailing new line. need to decode and strip to get string back.
        # e.g. b'700aa82a2b0c\n' -> '700aa82a2b0c'
        return subprocess.check_output(args).decode(self.encoding).strip()

    def _list_containers(self):
        return self._get_shell_output(
            ["docker", "ps", "--format", "table {{.ID}}\t{{.Names}}"]
        )

    def _name_to_id(self, container_name):
        container_id = self._get_shell_output(
            ["docker", "ps", "-aqf", f"name={container_name}"]
        )
        if not container_id:
            # TODO: hide the trace unless the fire -- --trace arg is passed.
            containers = self._list_containers()
            raise Exception(
                f"container not found with name {container_name}.\nchoose one of the following:\n{containers}"
            )

        return container_id

    def _id_to_logpath(self, container_id):
        log_path = self._get_shell_output(
            ["docker", "inspect", "--format='{{.LogPath}}'", container_id]
        )
        if not log_path:
            raise Exception(f"log_path not found for container {container_id}")

        return log_path

    # could use log_path, but keeping this function here for consistency. i.e. _id_to_logpath etc.
    # and keeping log_path so it's runnable from the cli.
    def _name_to_logpath(self, container_name):
        container_id = self._name_to_id(container_name)
        log_path = self._id_to_logpath(container_id)
        return log_path

    def log_path(self, container_name):
        """gets the path to the logfile in the vm for a container name"""
        return self._name_to_logpath(container_name)

    def cat_log(self, container_name):
        """prints the log to stdout"""
        container_id = self._name_to_id(container_name)
        return self._get_shell_output(["docker", "logs", container_id])

    def clear_log(self, container_name):
        """clears the log file without deleting it"""
        log_path = self._name_to_logpath(container_name)
        # start screen
        os.system(f"screen -dmS {self.screen_name} {self.vm_path}")

        # remove contents of log file, but don't remove the logfile itself.
        clear_log_command = f"echo '' > {log_path}"

        # finally working TODO: refactor to use subprocess?
        # https://stackoverflow.com/questions/42527291/clear-logs-in-native-docker-on-mac
        os.system(f'screen -S {self.screen_name} -p 0 -X stuff $"{clear_log_command}"')
        os.system(f'screen -S {self.screen_name} -p 0 -X stuff $"\n"')
        os.system(f"screen -S {self.screen_name} -X quit")
        print(f"Logs cleared for {container_name}")


if __name__ == "__main__":
    fire.Fire(DockerLogs)
