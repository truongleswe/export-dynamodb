"""
Export DynamoDb Module
"""
import click
import json
from boto3 import resource
from decimal import Decimal


@click.command()
@click.option('--table', '-t', help='table name.')
@click.option('--format', '-f', help='format file.', default='csv')
@click.option('--output', '-o', help='output filename.', default=None)
def main(table, format, output):
    """Export DynamoDb Table."""
    print('export dynamodb: {}'.format(table))
    data = read_dynamodb_data(table)
    if format != 'csv':
        write_to_json_file(data, table + '.json')


def read_dynamodb_data(table):
    """
    Scan all item from dynamodb.
    :param table: String
    :return: Data in Dictionary Format.
    """
    dynamodb_resource = resource('dynamodb')
    table = dynamodb_resource.Table(table)
    raw_data = table.scan()
    if raw_data is None:
        return None
    return raw_data['Items']

def convert_rawdata_to_stringvalue(data):
    """
    Convert raw data to string value.
    :param data: List of dictionary
    :return: String value.
    """
    ret = []
    for item in data:
        obj = {}
        for k, v in item.items():
            obj[k] = str(v)
        ret.append(obj)
    return ret

def convert_to_csv(data):
    """
    convert to csv.

    :param data: dictionary
    :return: None
    """
    pass

def write_to_json_file(data, filename):
    """
    Write to a json file
    :param data: Dictionary
    :param filename: output file name.
    :return: None
    """
    if data is None:
        return

    with open(filename, 'w') as f:
        f.write(json.dumps(convert_rawdata_to_stringvalue(data)))

def write_to_csv_file(data, filename):
    """
    Write to a csv file.
    :param data:
    :param filename:
    :return:
    """
    pass