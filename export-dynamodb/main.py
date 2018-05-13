import click

@click.command()
@click.option('--table', help='Name of table to export.')
def main(table):
    print('Dynamodb: {}'.format(table))

if __name__ == '__main__':
    main()