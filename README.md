[![Build Status](https://github.com/ConorSheehan1/osxdocker/workflows/ci/badge.svg)](https://github.com/ConorSheehan1/osxdocker/actions/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/ConorSheehan1/osxdocker)](https://github.com/ConorSheehan1/osxdocker/Pipfile)

# osxdocker
This is a small CLI for working with docker on OSX.
Currently it only handles docker logs, because I found it annoying starting up a screen session to get to the docker vm every time I wanted to clear logs.
See: https://stackoverflow.com/questions/42527291/clear-logs-in-native-docker-on-mac

### Usage
```bash
# list available commands
osxdocker

# get log path
osxdocker log_path $some_container_name

# clear logs
osxdocker clear_log $some_container_name
```

### Dev Install
```bash
pipenv install
pipenv run local_install
pipenv run osxdocker
```

### Dev tools
I set this project up using https://github.com/takluyver/flit/

```bash
flit --repository testpypi publish
```