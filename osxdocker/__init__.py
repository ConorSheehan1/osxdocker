"""
A CLI for working with docker on OSX
"""

__version__ = "0.0.2"


import fire
from .docker_logs import DockerLogs


def main():
    fire.Fire(DockerLogs)
