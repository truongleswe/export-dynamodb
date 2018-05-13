import click

@click.command()
@click.option('--table', '-t', help='table name.')
def main(table):
    print('Dynamodb: {}'.format(table))

if __name__ == '__main__':
    main()