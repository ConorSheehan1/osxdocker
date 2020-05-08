[![Build Status](https://github.com/ConorSheehan1/osxdocker/workflows/ci/badge.svg)](https://github.com/ConorSheehan1/osxdocker/actions/)
[![Documentation Status](https://readthedocs.org/projects/osxdocker/badge/?version=latest)](https://osxdocker.readthedocs.io)
[![PyPI](https://img.shields.io/pypi/v/osxdocker)](https://pypi.org/project/osxdocker/)
[![PyPI - License](https://img.shields.io/pypi/l/osxdocker)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# osxdocker
A CLI for working with docker on OSX

Currently it just handles docker logs, because I found it annoying starting up a screen session to get to the docker vm every time I wanted to clear logs. 
See: https://stackoverflow.com/questions/42527291/clear-logs-in-native-docker-on-mac

## Install
```bash
# python3 only
pip3 install osxdocker
```

## Dependencies
Assumes you have `docker` and `screen` installed. If you don't, you can easily install them through [brew](https://brew.sh/). e.g.
```
brew cask install docker
brew install screen
```

## Usage
```bash
# clear logs
osxdocker clear_log $some_container_name

# list available commands and flags
osxdocker
```

![clear_log_example](docs/source/images/clear_log_example.png)

This cli uses https://github.com/google/python-fire  
Check out the docs for more details on usage, setting up bash completion, etc.  
Also worth noting:
1. Because the package uses fire, it can be imported like a normal python package. e.g.
    ```python
    from osxdocker.docker_logs import DockerLogs
    DockerLogs().log_path('foo')
    ```
2. This cli doesn't support `--version` due to a quirk with fire.
    ```bash
    osxdocker version # works fine
    osxdocker --version # won't work
    ```

#### Edge cases and gotchas
Container names are unique, but containers are filtered by regex, so you can still run into issues.  
e.g. You have two containers, named foo and foo_too.  
`osxdocker cat_log foo` will fail because it matches foo and foo_too.  
`osxdocker cat_log ^foo$` will work because it matches foo exactly.

![multiple_container_error](docs/source/images/multiple_container_error.png)

#### Developer notes
See [docs/source/dev.md](docs/source/dev.md)
