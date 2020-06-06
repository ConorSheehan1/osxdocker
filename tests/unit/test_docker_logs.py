# Standard Library
import unittest
from unittest.mock import call, patch

# osxdocker
from osxdocker.docker_logs import DockerLogs


class TestDockerLogs(unittest.TestCase):
    def setUp(self):
        self.vm_path = "/temp/test_osxdocker/vm/path"
        self.screen_name = "test_screen"
        self.docker_logs = DockerLogs(screen_name=self.screen_name, vm_path=self.vm_path)
        self.container_name = "osxdocker-test"

    @patch("subprocess.check_output")
    def test_clear_log(self, check_output_mock):
        """
        This test covers clear_log and log_path,
        because clear_log uses _name_to_logpath and log_path is a wrapper for _name_to_logpath
        """
        check_output_mock.side_effect = [
            b"fake_docker_id\n",  # _name_to_id
            b"/temp/test_osxdocker/vm/path/fake_docker_id\n",  # _id_to_logpath
            b"\n",  # start screen as daemon
            b"\n",  # send clear log command
            b"\n",  # send newline char to run command
            b"\n",  # exit screen daemon
        ]
        clear_log_command = f"echo '' > /temp/test_osxdocker/vm/path/fake_docker_id"
        calls = [
            call(["docker", "ps", "-qf", f"name={self.container_name}"]),
            call(["docker", "inspect", "--format='{{.LogPath}}'", "fake_docker_id"]),
            call(f"screen -dmS {self.screen_name} {self.vm_path}", shell=True),
            call(f'screen -S {self.screen_name} -p 0 -X stuff $"{clear_log_command}"', shell=True),
            call(f'screen -S {self.screen_name} -p 0 -X stuff $"\n"', shell=True),
            call(f"screen -S {self.screen_name} -X quit", shell=True),
        ]

        self.docker_logs.clear_log(self.container_name)
        check_output_mock.assert_has_calls(calls)

    @patch("subprocess.check_output")
    def test_cat_log(self, check_output_mock):
        check_output_mock.side_effect = [
            b"fake_docker_id\n",  # _name_to_id
            b"/temp/test_osxdocker/vm/path/fake_docker_id\n",  # docker logs
        ]
        calls = [
            call(["docker", "ps", "-qf", f"name={self.container_name}"]),
            call(["docker", "logs", "fake_docker_id"]),
        ]

        self.docker_logs.cat_log(self.container_name)
        check_output_mock.assert_has_calls(calls)
