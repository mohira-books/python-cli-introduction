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
