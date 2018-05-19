Export DynamoDb Cli

Overview
========
export-dynamodb cli scan sequentially through all your dynamodb items. it supports to export to
either csv or json format.

Prerequisite
============

You must have at least Python 3.6 to run export-dynamodb cli tool.

export-dynamodb does not support to authenticate with AWS. You must be able to set
**AWS_ACCESS_KEY_ID** and **AWS_SECRET_ACCESS_KEY** to your environment variable. Refer
https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html to learn how you can
set these keys to your environment.

.. code-block:: bash

    # Install export-dynamodb
    $ pip install export-dynamodb

    # List of all export-dynamodb cli options.
    $ export-dynamodb --help

    # Export table and write to TABLE_NAME.csv file
    $ export-dynamodb -t TABLE_NAME -f csv

    # Export table and write to output.csv file
    $ export-dynamodb -t TABLE_NAME -f csv -o output.csv
