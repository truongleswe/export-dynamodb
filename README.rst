export-dynamodb
===============
A cli to export dynamodb.

**Key Features**
* Scan table in single or parallel thread.
* Output file can be json or csv.
* Get list of tables from yaml file.

How To Use
==========

.. code:: bash

$ pip install export-dynamodb
$ export-dynamodb --help

Getting Started
===============

.. code:: bash

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

# Upload new version
twine upload dist/*
