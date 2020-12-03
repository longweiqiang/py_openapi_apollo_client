#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/3 14:13
# @Author  : Weiqiang.long
# @Site    : 
# @File    : setup.py.py
# @Software: PyCharm
# @Description:

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "py_openapi_apollo_client",
    version = "1.0.0",
    author = "Weiqiang.long",
    description = "python-apollo客户端封装",
    long_description = long_description,
    long_description_content_type="text/markdown",
    url = "https://github.com/longweiqiang/py_openapi_apollo_client",
    packages = setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]

)