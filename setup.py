#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = dict(
    name='paragraph_shuffle',
    version='0.1.dev0',
    packages=['parshuffle', 'tests'],
    package_data={"tests": ['./data/paragraphs.txt']},
    url='',
    license='CC0 1.0 Universal',
    author='Imrich Štoffa',
    author_email='imostoffa@gmail.com',
    description='Shuffle paragraphs in text file'
)

setup(**config)
