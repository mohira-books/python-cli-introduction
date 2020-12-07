# その2: Pythonでコマンドを作ろう 後編

## 参考

- [pypa/sampleproject: A sample project that exists for PyPUG's "Tutorial on Packaging and Distributing Projects"](https://github.com/pypa/sampleproject)
- [Packaging and distributing projects — Python Packaging User Guide](https://packaging.python.org/guides/distributing-packages-using-setuptools/#setup-py)

## 目標
- 次のようなコマンドをつくる
- 直下ではなくパッケージを使った場合

```
$ hey
HEY!!!
```

```
# ディレクトリ構成
python-cli-introduction
├── README.md
├── goodbye.py
├── hello.py
├── requirements.txt
├── setup.py
└── src
    ├── __init__.py
    └── cli
        ├── __init__.py
        └── hey.py
```

### `src/cli/hey.py`
```python
def main():
    print('HEY!!!')


if __name__ == '__main__':
    main()

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

    entry_points={'console_scripts': ['hello=hello:main',
                                      'goodbye=goodbye:main',
                                      'hey=src.cli.hey:main',]}
)
```
