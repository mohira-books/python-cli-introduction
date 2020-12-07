import click


@click.command()
@click.argument('name')
def main(name: str):
    """相手の名前を叫ぶコマンド"""
    message = f'{name.upper()}!!!'

    click.echo(message)


if __name__ == '__main__':
    main()
