### Dev Install
```bash
poetry install

# install osxdocker as symlink to avoid reinstall whenever code changes
# https://github.com/python-poetry/poetry/issues/1135
# workaround using __name__ == '__main__' and fire
poetry run task dev_osxdocker
```

### Test pypi install
```bash
# install from test pypi, allow pull from non-test pypi for fire
pip3 install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple osxdocker
```

### Dev tools
#### Deploy
https://github.com/python-poetry/poetry manages building and deploying
Will either need `~/.pypirc` set up, or pass the `--username` and `--password` to publish commands.

A github action pushes every git tag to pypi.
A webhook polls the github repo to keep the docs in sync.

```bash
# build dist
poetry build

# publish to test pypi https://github.com/python-poetry/poetry/issues/742#issuecomment-609642943
poetry config repositories.testpypi https://test.pypi.org/legacy/
poetry publish --repository testpypi

# really publish
poetry publish
```

#### Tests
```bash
poetry run task tests
```

#### Linter
```bash
# to autoformat python code
poetry run task lint

# to sort imports
poetry run task isort
```

#### Docs
```bash
poetry run task build_docs
```

#### Version management
```bash
# pass args e.g. patch, minor, major
poetry run bumpversion --commit --tag patch

# typical release cycle
poetry run bumpversion --commit --tag patch
poetry run task tests
poetry run task ci_lint
poetry publish --build
```
Source of truth is .bumpversion.cfg.
See https://github.com/ConorSheehan1/osxdocker/issues/7 and https://github.com/python-poetry/poetry/issues/144#issuecomment-440061951
