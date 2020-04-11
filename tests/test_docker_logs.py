# Standard Library
import subprocess
import unittest

# Third party
import docker

# osxdocker
from osxdocker.docker_logs import DockerLogs


class TestDockerLogs(unittest.TestCase):
    def setUp(self):
        self.docker_logs = DockerLogs()
        self.container_name = "osxdocker-test"
        self.client = docker.from_env()
        self.client.containers.run(
            "ubuntu:18.04", "echo hello world", name=self.container_name, detach=True
        )

    def tearDown(self):
        self.client.api.remove_container(self.container_name, force=True)

    def test_cat_log(self):
        assert self.docker_logs.cat_log(self.container_name) == "hello world"

    def test_clear_log(self):
        self.docker_logs.clear_log(self.container_name)
        assert self.docker_logs.cat_log(self.container_name) == ""


class TestDockerLogsNoContainer(unittest.TestCase):
    def setUp(self):
        self.docker_logs = DockerLogs(debug=True)
        self.container_name = "osxdocker-test"

    def test_no_container_exception(self):
        with self.assertRaises(Exception) as context:
            self.docker_logs.cat_log(self.container_name)

        # GOTCHA: test will pass regardless of this assertion, if indented withing assertRaises context manager
        self.assertIn(
            f"could not find container matching name '{self.container_name}'.",
            str(context.exception),
        )


class TestDockerLogsMultipleContainers(unittest.TestCase):
    def setUp(self):
        self.docker_logs = DockerLogs(debug=True)
        self.container_name = "osxdocker-test"
        self.client = docker.from_env()
        for i in range(2):
            self.client.containers.run(
                "ubuntu:18.04",
                "echo hello world",
                name=f"{self.container_name}{i}",
                detach=True,
            )

    def tearDown(self):
        for i in range(2):
            self.client.api.remove_container(f"{self.container_name}{i}", force=True)

    def test_multiple_container_exception(self):
        # containers are run in detached mode, so wait for last one to start
        self.client.api.wait(f"{self.container_name}1")

        with self.assertRaises(Exception) as context:
            self.docker_logs.cat_log(self.container_name)

        self.assertIn(
            f"multiple containers found matching name '{self.container_name}'. Run `docker ps -af name={self.container_name}` for details.",
            str(context.exception),
        )
