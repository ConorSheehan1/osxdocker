[![Build Status](https://github.com/ConorSheehan1/osxdocker/workflows/ci/badge.svg)](https://github.com/ConorSheehan1/osxdocker/actions/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/ConorSheehan1/osxdocker)](https://github.com/ConorSheehan1/osxdocker/Pipfile)

# osxdocker
This is a small CLI for working with docker on OSX.
Currently it only handles docker logs, because that was an issue for me on OSX.
See: https://stackoverflow.com/questions/42527291/clear-logs-in-native-docker-on-mac

### Dev Install
```
pipenv install
pipenv run local_install
pipenv run osxdocker
```

### Example usage
```
pipenv run osxdocker clear_log some_container_name
```