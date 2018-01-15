#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

__author__ = '袁书辉'

import os
from zipfile import *
import zipfile


# 解压zip文件
def unzip():
    source_zip = "c:\\update\\SW_Servers_20120815.zip"
    target_dir = "c:\\update\\"
    myzip = ZipFile(source_zip)
    myfilelist = myzip.namelist()
    for name in myfilelist:
        f_handle = open(target_dir + name, "wb")
        f_handle.write(myzip.read(name))
        f_handle.close()
    myzip.close()


# 添加文件到已有的zip包中
def addzip():
    f = zipfile.ZipFile('archive.zip', 'w', zipfile.ZIP_DEFLATED)
    f.write('file_to_add.py')
    f.close()


# 把整个文件夹内的文件打包
def adddirfile(startdir,outZipPath):
    f = zipfile.ZipFile(outZipPath+'/archive.zip', 'w', zipfile.ZIP_DEFLATED)

    for dirpath, dirnames, filenames in os.walk(startdir):
        print  dirnames,dirpath
        for filename in filenames:
            print filename+'ssfsdfsd'

            f.write(os.path.join(dirpath, filename),filename)
    f.close()
    return '/archive.zip'
