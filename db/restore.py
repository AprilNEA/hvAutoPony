#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @author: sukeycz
# @license:
# @contact: sukeycz0@gmail.com
# @software: PyCharm
# @project : hvAutoPony
# @file: restore.py
# @time: 2021/6/5 21:20
# @desc:
import sqlite

data = []
class User():
    def __init__(self,uid,name,password,genre,counter,charges,counter_all):
        self.uid=uid
        self.name=name
        self.password=password
        self.genre=genre
        self.charges=charges
        self.counter=counter
        self.counter_all=counter_all

# sqlite.create_db()
for i in data:
    i2 = User(i["UID"],i["NAME"],i["PASS"],i["GENRE"],i["counter"],i["charges"],i["counter_all"])
    sqlite.user_add(i2)
