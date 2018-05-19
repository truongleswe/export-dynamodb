"""
Export DynamoDb Module
"""
import click
import json
import csv
from boto3 import resource


@click.command()
@click.option('--table', '-t', help='table name.')
@click.option('--format', '-f', help='format file [csv/json].', default='csv')
@click.option('--output', '-o', help='output filename.', default=None)
def main(table, format, output):
    """Export DynamoDb Table."""
    print('export dynamodb: {}'.format(table))
    data = read_dynamodb_data(table)
    if format != 'csv':
        output_filename = table + '.json'
        if output is not None:
            output_filename = output
        write_to_json_file(data, output_filename)
    else:
        output_filename = table + '.csv'
        if output is not None:
            output_filename = output
        write_to_csv_file(data, output_filename)

def get_keys(data):
    keys = set([])
    for item in data:
        keys = keys.union(set(item.keys()))
    return keys

def read_dynamodb_data(table):
    """
    Scan all item from dynamodb.
    :param table: String
    :return: Data in Dictionary Format.
    """
    print('Connecting to AWS DynamoDb')
    dynamodb_resource = resource('dynamodb')
    table = dynamodb_resource.Table(table)
    print('Downloading ', end='')
    raw_data = table.scan()
    if raw_data is None:
        return None
    items = raw_data['Items']
    keys = set([]).union(get_keys(items))
    print("{} records".format(raw_data['Count']))
    while raw_data.get('LastEvaluatedKey'):
        print('Downloading ', end='')
        raw_data = table.scan(ExclusiveStartKey=raw_data['LastEvaluatedKey'])
        items.extend(raw_data['Items'])
        keys = keys.union(get_keys(items))
        print("{} records".format(raw_data['Count']))
    print("Total downloaded records: {}".format(len(items)))
    return {'items': items, 'keys': keys}

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

def write_to_json_file(data, filename):
    """
    Write to a json file
    :param data: Dictionary
    :param filename: output file name.
    :return: None
    """
    if data is None:
        return

    print("Writing to json file.")
    with open(filename, 'w') as f:
        f.write(json.dumps(convert_rawdata_to_stringvalue(data['items'])))

def write_to_csv_file(data, filename):
    """
    Write to a csv file.
    :param data:
    :param filename:
    :return:
    """
    if data is None:
        return

    print("Writing to csv file.")
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=data['keys'],
                                quotechar='"')
        writer.writeheader()
        writer.writerows(data['items'])