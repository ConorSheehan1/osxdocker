# Standard Library
import unittest
from unittest.mock import patch, call

# osxdocker
from osxdocker.docker_logs import DockerLogs


class TestDockerLogs(unittest.TestCase):
    def setUp(self):
        self.vm_path = '/temp/test_osxdocker/vm/path'
        self.screen_name = 'test_screen'
        self.docker_logs = DockerLogs(screen_name=self.screen_name, vm_path=self.vm_path)
        self.container_name = "osxdocker-test"

    @patch('subprocess.call')
    @patch('subprocess.check_output')
    def test_clear_log(self, check_output_mock, call_mock):
        check_output_mock.side_effect = [
            b"fake_docker_id\n", # _name_to_id
            b"/temp/test_osxdocker/vm/path/fake_docker_id\n", # _id_to_logpath
        ]
        clear_log_command = f"echo '' > /temp/test_osxdocker/vm/path/fake_docker_id"

        self.docker_logs.clear_log(self.container_name)
        check_output_mock.assert_has_calls([
            call(["docker", "ps", "-qf", f"name={self.container_name}"]), # _name_to_id
            call(['docker', 'inspect', "--format='{{.LogPath}}'", 'fake_docker_id']), # _id_to_logpath
        ])
        call_mock.assert_has_calls([
            call(f"screen -dmS {self.screen_name} {self.vm_path}", shell=True), # start screen as daemon
            call(f'screen -S {self.screen_name} -p 0 -X stuff $"{clear_log_command}"', shell=True), # send clear log command
            call(f'screen -S {self.screen_name} -p 0 -X stuff $"\n"', shell=True), # send newline char to run command
            call(f"screen -S {self.screen_name} -X quit", shell=True), # exit screen daemon
        ])


