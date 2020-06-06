# Standard Library
import subprocess

# Third party
import fire
from termcolor import colored

# osxdocker
from osxdocker.utils.docker_base import DockerBase


class DockerLogs(DockerBase):
    """
    A module for interacting with docker logs.

    Example:
        >>> from osxdocker.docker_logs import DockerLogs
        >>> DockerLogs().log_path('foo')
    """

    # could use _name_to_logpath, but keeping this function here for consistency. i.e. _id_to_logpath etc.
    # and keeping log_path so it's runnable from the cli.
    def log_path(self, container_name: str) -> str:
        """
        Returns the path to the log on the docker vm.

        Args:
            container_name: name of the target container.
        """
        return self._name_to_logpath(container_name)

    def cat_log(self, container_name: str) -> str:
        """
        Returns the content of the log.

        Args:
            container_name: name of the target container.
        """
        container_id = self._name_to_id(container_name)
        return self._get_shell_output(["docker", "logs", container_id])

    def clear_log(self, container_name: str):
        """
        Clears the log file without deleting it.

        Args:
            container_name: name of the target container.
        """
        log_path = self._name_to_logpath(container_name)
        clear_log_command = f"echo '' > {log_path}"
        commands = [
            f"screen -dmS {self.screen_name} {self.vm_path}",  # start screen as daemon
            f'screen -S {self.screen_name} -p 0 -X stuff $"{clear_log_command}"',  # remove contents of log file, but don't remove the logfile itself.
            f'screen -S {self.screen_name} -p 0 -X stuff $"\n"',  # send newline char to run command
            f"screen -S {self.screen_name} -X quit",  # exit screen
        ]
        for command in commands:
            subprocess.check_output(command, shell=True)

        print(colored(f"Logs cleared for '{container_name}'", "green"))


if __name__ == "__main__":
    fire.Fire(DockerLogs)
