[![Build Status](https://github.com/ConorSheehan1/osxdocker/workflows/ci/badge.svg)](https://github.com/ConorSheehan1/osxdocker/actions/)
[![PyPI](https://img.shields.io/pypi/v/osxdocker)](https://pypi.org/project/osxdocker/)
[![PyPI - License](https://img.shields.io/pypi/l/osxdocker)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/ConorSheehan1/osxdocker)](https://github.com/ConorSheehan1/osxdocker/blob/master/Pipfile)

# osxdocker
A CLI for working with docker on OSX 

Currently it only handles docker logs, because I found it annoying starting up a screen session to get to the docker vm every time I wanted to clear logs.
See: https://stackoverflow.com/questions/42527291/clear-logs-in-native-docker-on-mac

# Install
```bash
pip install osxdocker
```

### Usage
```bash
# clear logs
osxdocker clear_log $some_container_name

# get log path
osxdocker log_path $some_container_name

# list available commands
osxdocker
```

### Dev Install
```bash
# install dev dependencies, install package as symlink to avoid reinstall whenever code changes
pipenv install
pipenv run local_install
pipenv run osxdocker # only runs from pipenv in dev
```

```bash
# install from test pypi, allow pull from non-test pypi for fire
pip3 install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple osxdocker
```

### Dev tools
I set this project up using https://github.com/takluyver/flit/

```bash
# build dist
pipenv run flit build

# publish to test pypi
pipenv run publish_test

# really publish
pipenv run publish
```