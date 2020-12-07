import click


@click.command()
@click.argument('name')
def main(name: str):
    """あいさつするコマンド"""
    message = f'Hello! {name}'

    click.echo(message)


if __name__ == '__main__':
    main()
