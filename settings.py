#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @author: sukeycz
# @license:
# @contact: sukeycz0@gmail.com
# @software: PyCharm
# @project : hvAutoPony
# @file: settings.py.py
# @time: 2021/6/6 17:38
# @desc:
import os

RootDirectory = "D:\Github\hvAutoPony"#os.getcwd()
PublicDirectory = os.path.join(RootDirectory, "public")
DatabaseLocation = os.path.join(RootDirectory, "src\db")

if __name__ == '__main__':
    print(RootDirectory,PublicDirectory,DatabaseLocation)
