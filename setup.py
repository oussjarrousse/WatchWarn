#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='watchtower',
    version='1.0',
    packages=find_packages(),

    license='All Rights Reserves to Oussama Jarrousse',
    long_description=open('README.md').read(),
    install_requires= [
        'Django',
        'djangorestframework',
        'django-filter',
        'django-crispy-forms',
    ]
)
