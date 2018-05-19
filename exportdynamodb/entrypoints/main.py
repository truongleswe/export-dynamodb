"""
Export DynamoDb Module
"""
import click
import json
import csv
from boto3 import resource


@click.command()
@click.version_option(version='2.0.1')
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
    keys = []
    for item in table.attribute_definitions:
        keys.append(item['AttributeName'])
    keys_set = set(keys)
    item_count = table.item_count

    raw_data = table.scan()
    if raw_data is None:
        return None

    items = raw_data['Items']
    fieldnames = set([]).union(get_keys(items))
    cur_total = (len(items) + raw_data['Count'])
    if cur_total > item_count:
        percents = 99.99
    else:
        percents = cur_total * 100 / item_count

    print("{} records ..... {:02.0f}%".format(raw_data['Count'], percents),
          end='\r')
    while raw_data.get('LastEvaluatedKey'):
        print('Downloading ', end='')
        raw_data = table.scan(ExclusiveStartKey=raw_data['LastEvaluatedKey'])
        items.extend(raw_data['Items'])
        fieldnames = fieldnames.union(get_keys(items))
        cur_total = (len(items) + raw_data['Count'])
        if cur_total > item_count:
            percents = 99.99
        else:
            percents = cur_total * 100 / item_count

        print("{} records ..... {:02.0f}%".format(raw_data['Count'], percents),
              end='\r')
    print("Total downloaded records: {}".format(len(items)))

    for fieldname in fieldnames:
        if fieldname not in keys_set:
            keys.append(fieldname)
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
