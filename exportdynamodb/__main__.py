import click

@click.command()
@click.option('--table', help='Table name.')
def main(table):
    print('Dynamodb: {}'.format(table))

if __name__ == '__main__':
    main()