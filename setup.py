#!/usr/bin/env python
from setuptools import setup

# Put here required packag
# Uncomment one or more lines below in the install_requires section
# for the specific client drivers/modules your application needs.
packages = ['tornado', 'pymongo', 'redis', 'PyMySQL3', 'peewee', 'pycket'
            ]

setup(name='LinkBook', version='0.0.1',
      description='OpenShift Python-3.3 / Tornado Web Server based application',
      author='LinkBook.L.U', author_email='admin@example.org',
      url='https://pypi.python.org/pypi',
      install_requires=packages,
      )
