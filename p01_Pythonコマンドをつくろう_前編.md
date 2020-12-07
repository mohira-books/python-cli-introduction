# その1: Pythonコマンドをつくろう 前編

## 参考

- [pypa/sampleproject: A sample project that exists for PyPUG's "Tutorial on Packaging and Distributing Projects"](https://github.com/pypa/sampleproject)
- [Packaging and distributing projects — Python Packaging User Guide](https://packaging.python.org/guides/distributing-packages-using-setuptools/#setup-py)

## 目標
次のようなコマンドをつくる

```
$ hello
Hello World!
```

## 手順
### `hello.py`

```python
def main():
    print('Hello World!')


if __name__ == '__main__':
    main()
```

### `setup.py`

- [Python モジュールの配布 — Python 3.9.1 ドキュメント](https://docs.python.org/ja/3/distributing/index.html#distributing-index)
- [Packaging and distributing projects — Python Packaging User Guide](https://packaging.python.org/guides/distributing-packages-using-setuptools/?highlight=entry_points)

```python
from setuptools import setup, find_packages

setup(
    # パッケージに関するメタ情報を記述
    name='mycmd',
    version='0.0.1',
    packages=find_packages(),
    url='',
    license='MIT',
    author='mohira',
    author_email='mohira@example.com',
    description='',

    # https://packaging.python.org/guides/distributing-packages-using-setuptools/?highlight=entry_points#entry-points
    entry_points={'console_scripts': ['hello=hello:main']}
)
```

### `install` する

- Editable install を行う

```
$ pip install -e .
```

installされていることを確認する。

```
$ pip list
Package    Version Location
---------- ------- -----------------------------------------------------------------
mycmd      0.0.1   /project_dir/python-cli-introduction
pip        20.3.1
setuptools 51.0.0
```

### 確認
- うまくいったら、`hello.py`の記述を変更してみよう

```
$ hello
Hello World!
```



## 演習
次のようなコマンドを追加しましょう

```
$ goodbye
Good Bye!
```

### `goodbye.py`

```python
def main():
    print('Good Bye!')


if __name__ == '__main__':
    main()
```

### `setup.py`

```python
from setuptools import setup, find_packages

setup(
    name='mycmd',
    version='0.0.1',
    packages=find_packages(),
    url='',
    license='MIT',
    author='mohira',
    author_email='mohira@example.com',
    description='',

    entry_points={'console_scripts': ['hello=hello:main',
                                      'goodbye=goodbye:main', ]}
)
```

以上