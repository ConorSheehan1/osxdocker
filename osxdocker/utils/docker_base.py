# Standard Library
import subprocess
from typing import List

# osxdocker
from osxdocker import __version__
from osxdocker.utils.warn import warn


class DockerBase:
    """
    The base module for osxdocker.

    Args:
        debug: show full stack trace if true by raising exception. otherwise print warning. Default: false
        screen_name: name to use for screen daemon. Default: osxdocker
        encoding: encoding to use for shell. Default: utf-8
        vm_path: path to docker vm. Default: ~/Library/Containers/com.docker.docker/Data/vms/0/tty
    """

    def __init__(
        self,
        debug: bool = False,
        screen_name: str = "osxdocker",
        encoding: str = "utf-8",
        vm_path: str = "~/Library/Containers/com.docker.docker/Data/vms/0/tty",
    ):
        self.debug = debug
        self.screen_name = screen_name
        self.encoding = encoding
        self.vm_path = vm_path

        # can't use --version, adding version arg to __init__ seems to open help screen.
        # if version:
        #     print(__version__)

    def version(self):
        """
        Prints the version of osxdocker.
        """
        print(__version__)

    def _get_shell_output(self, args: List[str]) -> str:
        # subprocess stdout is in bytes with trailing new line. need to decode and strip to get string back.
        # e.g. b'700aa82a2b0c\n' -> '700aa82a2b0c'
        return subprocess.check_output(args).decode(self.encoding).strip()

    def _list_containers(self) -> str:
        return self._get_shell_output(["docker", "ps", "--format", "table {{.ID}}\t{{.Names}}"])

    def _ids_by_name(self, container_name: str, stopped: bool = False) -> str:
        """
        gets docker container ids by name.
        helper for name_to_id.
        """
        # -a (ALL) show all containers, not just running ones
        # -q (Quiet) list ids only
        # -f (Filter) filter by name
        arg = "-aqf" if stopped else "-qf"
        return self._get_shell_output(["docker", "ps", arg, f"name={container_name}"])

    def _name_to_id(self, container_name: str) -> str:
        """
        Gets the id of a container using its name.
        Searches running containers first, then stopped containers if it doesn't find a match.

        Raises:
            Exception: if no containers are found, or multiple containers are found
        """
        container_id = self._ids_by_name(container_name)
        if not container_id:
            container_id = self._ids_by_name(container_name, stopped=True)

        if not container_id:
            message = f"could not find container matching name '{container_name}'."
            containers = self._list_containers()
            if containers.count("\n") > 0:
                message += f"\nchoose one of the following:\n{containers}"
            warn(message, self.debug)

        if "\n" in container_id:
            warn(
                f"multiple containers found matching name '{container_name}'. Run `docker ps -af name={container_name}` for details.",
                self.debug,
            )

        return container_id

    def _id_to_logpath(self, container_id: str) -> str:
        log_path = self._get_shell_output(
            ["docker", "inspect", "--format='{{.LogPath}}'", container_id]
        )

        if not log_path:
            warn(f"log_path not found for container '{container_id}'.", self.debug)

        return log_path

    def _name_to_logpath(self, container_name: str) -> str:
        container_id = self._name_to_id(container_name)
        log_path = self._id_to_logpath(container_id)
        return log_path
