"""
A python CLI for working with docker on OSX
"""

__version__ = "0.0.1"


import fire
from .docker_logs import DockerLogs


def main():
    fire.Fire(DockerLogs)
