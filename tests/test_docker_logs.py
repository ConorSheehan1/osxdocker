import os
import docker
import unittest
from osxdocker.docker_logs import DockerLogs


class TestDockerLogs(unittest.TestCase):
    def setUp(self):
        client = docker.from_env()
        self.docker_logs = DockerLogs()
        self.container_name = "osxdocker-test"
        client.containers.run(
            "ubuntu:18.04", "echo hello world", name=self.container_name, detach=True
        )

    def tearDown(self):
        os.system(f"docker rm {self.container_name}")

    def test_cat_log(self):
        assert self.docker_logs.cat_log(self.container_name) == "hello world"

    def test_clear_log(self):
        self.docker_logs.clear_log(self.container_name)
        assert self.docker_logs.cat_log(self.container_name) == ""
