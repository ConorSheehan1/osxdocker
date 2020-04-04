# osxdocker
This is a small CLI for working with docker on OSX.
Currently it only handles docker logs, because that was an issue for me on OSX.
See: https://stackoverflow.com/questions/42527291/clear-logs-in-native-docker-on-mac

### Install
```
pipenv install
pipenv run local_install
pipenv run osxdocker
```

### Example usage
```
pipenv run osxdocker clear_log some_container_name
```