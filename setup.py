#!/usr/bin/env python
import os, sys
import shutil
import datetime

from setuptools import setup, find_packages
from setuptools.command.install import install

readme = open('README.md').read()

VERSION = '0.2'

requirements = [
    'torch',
]
setup(
    # Metadata
    name='torchlop',
    version=VERSION,
    author='Hahn Yuan',
    author_email='yuanzhihang1@126.com',
    url='https://github.com/hahnyuan/pytorch-layerwise-OpCounter/',
    description='A tool to layer-wise count the MACs and parameters of PyTorch model.',
    long_description=readme,
    long_description_content_type='text/markdown',
    license='MIT',

    # Package info
    packages=find_packages(exclude=('*test*',)),

    #
    zip_safe=True,
    install_requires=requirements,

    # Classifiers
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
