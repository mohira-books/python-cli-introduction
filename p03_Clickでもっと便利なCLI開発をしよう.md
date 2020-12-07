# その3: Clickでもっと便利なCLI開発をしよう

## 参考

- [Setuptools Integration — Click Documentation (7.x)](https://click.palletsprojects.com/en/7.x/setuptools/)
- [Packaging and distributing projects — Python Packaging User Guide](https://packaging.python.org/guides/distributing-packages-using-setuptools/#setup-py)

## 目標
- 次のようなコマンドをつくる
- 直下ではなくパッケージを使った場合

```
$ greet Bob
Hello Bob! 

$ greet Tom
Hello Tom! 

$ greet Ken
Hello Ken! 
```

### install
```
$ pip install click
```

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
                                      'greet=src.cli.greet:main',]}
)
```

### install
```
$ pip install -e .
```

### `src/cli/greet.py`
```python
import click


@click.command()
@click.argument('name')
def main(name: str):
    """あいさつするコマンド"""
    message = f'Hello! {name}'

    click.echo(message)


if __name__ == '__main__':
    main()
```

### 実行してみる

```
$ greet Bob
Hello Bob! 

$ greet Tom
Hello Tom! 

$ greet Ken
Hello Ken! 
```


### helpが非常に便利
```
# helpも自動で生成してくれる
$ greet --help
Usage: greet [OPTIONS] NAME

  あいさつするコマンド

Options:
  --help  Show this message and exit.
```


## 演習
```
$ shout bob
BOB!!!

$ shout tom
Tom!!!

$ shout ken
Ken!!!
```


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
                                      ]}
)

```

### `src/cli/shout.py`
```python
import click


@click.command()
@click.argument('name')
def main(name: str):
    """相手の名前を叫ぶコマンド"""
    message = f'{name.upper()}!!!'

    click.echo(message)


if __name__ == '__main__':
    main()

```


### `install`
```
$ pip install -e .
```

### 実行
```
$ shout bob
BOB!!!

$ shout tom
Tom!!!

$ shout ken
Ken!!!
```

### help
```
$ shout --help
Usage: shout [OPTIONS] NAME

  相手の名前を叫ぶコマンド

Options:
  --help  Show this message and exit.
```