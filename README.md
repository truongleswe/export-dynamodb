# export_dynamodb
[![CircleCI](https://circleci.com/gh/travistrle/export-dynamodb/tree/master.svg?style=svg)](https://circleci.com/gh/travistrle/export-dynamodb/tree/master) 
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

A cli to export dynamodb. [export-dynamodb](https://pypi.org/project/export-dynamodb/) on pypi.

**Key Features**
  * Scan table in single or parallel thread.
  * Output file can be json or csv.
  * Get list of tables from yaml file.

## How To Use

```bash
$ pip install export-dynamodb
$ export-dynamodb --help
```

## Getting Started

```
# Install virtual environment
$ pip3 install virtualenv 
$ virtualenv -p python3 venv
$ source venv/bin/activate

# Install dependencies
$ pip install -r requirements.txt

# test cli local
pip install -e .

# if you want to exit from development environment, use deactivate command
$ deactivate

python setup.py sdist upload -r pypi

# Upload new version
$ brew install pandoc
$ which pandoc
$ python setup.py sdist
$ twine upload dist/*
```