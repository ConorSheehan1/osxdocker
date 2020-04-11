# Standard Library
import subprocess

# Third party
import fire
from termcolor import colored

# osxdocker
from osxdocker.utils.docker_base import DockerBase


class DockerLogs(DockerBase):
    # could use _name_to_logpath, but keeping this function here for consistency. i.e. _id_to_logpath etc.
    # and keeping log_path so it's runnable from the cli.
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
        # start screen as daemon
        subprocess.call(f"screen -dmS {self.screen_name} {self.vm_path}", shell=True)

        # remove contents of log file, but don't remove the logfile itself.
        clear_log_command = f"echo '' > {log_path}"
        subprocess.call(
            f'screen -S {self.screen_name} -p 0 -X stuff $"{clear_log_command}"',
            shell=True,
        )

        # # send new line char to run command
        subprocess.call(f'screen -S {self.screen_name} -p 0 -X stuff $"\n"', shell=True)
        subprocess.call(f"screen -S {self.screen_name} -X quit", shell=True)
        print(colored(f"Logs cleared for '{container_name}'", "green"))


if __name__ == "__main__":
    fire.Fire(DockerLogs)
