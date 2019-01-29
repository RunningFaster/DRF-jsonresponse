#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: RunningFaster
# Mail: Vladimir1993rj@gmail.com
# Created Time:  2019-1-29 10:10:10
#############################################
from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='drf_jsonresponse',
      version='0.1',

      description='DRF modifies mixins to return a custom jsonresponse',
      long_description=long_description,
      long_description_content_type="text/markdown",

      url='http://github.com/tongling/clinicaltrial',
      author="RunningFaster",
      author_email="Vladimir1993rj@gmail.com",
      license='MIT',

      packages=setuptools.find_packages(),
      install_requires=['Django==2.1.5', 'djangorestframework==3.9.1'],
      include_package_data=True,
      platforms="any",
      zip_safe=False)
