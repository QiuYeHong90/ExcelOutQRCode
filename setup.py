#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

__author__ = '袁书辉'

#coding:utf-8
#package project

from setuptools import setup, find_packages

setup(
    name="apmonitor",
    version="1.0.0",

    author="orangleliu",
    author_email="orangleliu@gmail.com",

    #自动寻找带有 __init__.py 的文件夹
    packages=find_packages(exclude=["logs"]),

    install_requires = ['django==1.6'],
    description = "ap monitor system",

    #单独的一些py脚本,不是在某些模块中
    scripts = ["dbrouters.py","index.py",
               "manage.py", "settings.py",
               "uwsgi.py", "__ini__.py"],

    #静态文件等，配合MANIFEST.in (package_data 参数不太好使)
    include_package_data = True,

    #如果是正式的项目，还会有更多的信息（例如开源证书写在下面）
    url = "http://wifi21.com",
)