"""
Export DynamoDb Module
"""
import click


@click.command()
@click.option('--table', '-t', help='table name.')
def main(table):
    """Export DynamoDb Table."""
    print('export dynamodb: {}'.format(table))