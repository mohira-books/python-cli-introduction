# その4: Clickでサブコマンドをつくろう

## 参考
- [Nesting Commands¶ ](https://click.palletsprojects.com/en/7.x/quickstart/#nesting-commands)



## 目標
```
$ calc add 3 4
3 + 4 = 7

$ calc sub 3 4
3 - 4 = -1

$ calc mul 3 4
3 * 4 = 12
```


## `setup.py` と install
### `setup.py`
```python
from setuptools import find_packages, setup

setup(
    name='mycmd',
    version='0.0.1',
    packages=find_packages(),
    url='',
    license='MIT',
    author='mohira',
    author_email='mohira@example.com',
    description='',

    install_requires=[
        'Click'
    ],

    entry_points={'console_scripts': ['hello=hello:main',
                                      'goodbye=goodbye:main',
                                      'hey=src.cli.hey:main',
                                      'greet=src.cli.greet:main',
                                      'shout=src.cli.shout:main',
                                      'calc=src.cli.calc:main',
                                      ]}
)
```

### install
```
$ pip install -e .
```

## `calc add`
```python
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


if __name__ == '__main__':
    main()
```


## `calc sub`
```python
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


if __name__ == '__main__':
    main()

```

## `calc mul`
```python
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
```

## helpをみる
```
$ calc --help
Usage: calc [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  add  2つの整数の和を計算するコマンド
  mul  2つの整数の積を計算するコマンド
  sub  2つの整数の差を計算するコマンド
```

```
$ calc add --help
Usage: calc add [OPTIONS] X Y

  2つの整数の和を計算するコマンド

Options:
  --help  Show this message and exit.
```

```
$ calc sub --help
Usage: calc sub [OPTIONS] X Y

  2つの整数の差を計算するコマンド

Options:
  --help  Show this message and exit.
```

```
$ calc mul --help
Usage: calc mul [OPTIONS] X Y

  2つの整数の積を計算するコマンド

Options:
  --help  Show this message and exit.
```