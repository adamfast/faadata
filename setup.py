#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='faadata',
    version='1.0.0',
    description='Models and load scripts used to import FAA (and FADDS) data into Django',
    author='Adam Fast',
    author_email='adamfast@gmail.com',
    url='https://github.com/adamfast/faadata',
    packages=find_packages(),
    package_data={
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)