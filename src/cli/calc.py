import click


@click.group()
def main():
    pass


@main.command()
@click.argument('x', type=click.INT)
@click.argument('y', type=click.INT)
def add(x: int, y: int):
    """2つの整数の和を計算するコマンド"""
    summation = x + y
    output = f'{x} + {y} = {summation}'

    click.echo(output)


@main.command()
@click.argument('x', type=click.INT)
@click.argument('y', type=click.INT)
def sub(x: int, y: int):
    """2つの整数の差を計算するコマンド"""
    difference = x - y
    output = f'{x} - {y} = {difference}'

    click.echo(output)


@main.command()
@click.argument('x', type=click.INT)
@click.argument('y', type=click.INT)
def mul(x: int, y: int):
    """2つの整数の積を計算するコマンド"""
    product = x * y
    output = f'{x} * {y} = {product}'

    click.echo(output)


if __name__ == '__main__':
    main()
