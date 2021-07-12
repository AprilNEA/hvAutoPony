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

data = [
    {'UID': 4697311, 'NAME': 'Grandmasters', 'PASS': '781898', 'GENRE': '0', 'counter': '21418', 'charges': 299953227,
     'counter_all': 46773},
    {'UID': 5098427, 'NAME': 'yama', 'PASS': '225500', 'GENRE': '0', 'counter': '17', 'charges': 5896,
     'counter_all': 1305},
    {'UID': 0, 'NAME': '0000', 'PASS': '781898', 'GENRE': '0', 'counter': '12376', 'charges': 964705,
     'counter_all': 35389},
    {'UID': 565719, 'NAME': 'ss', 'PASS': '565719', 'GENRE': '0', 'counter': '8314', 'charges': 99999965436,
     'counter_all': 40640},
    {'UID': 1372927, 'NAME': 'Despair', 'PASS': '272937', 'GENRE': '0', 'counter': '12958', 'charges': 99960562,
     'counter_all': 40061},
    {'UID': 3146277, 'NAME': 'AM', 'PASS': '131477', 'GENRE': '0', 'counter': '368', 'charges': 1206,
     'counter_all': 2381},
    {'UID': 975311, 'NAME': 'czx', 'PASS': '113759', 'GENRE': '0', 'counter': '36', 'charges': 2784,
     'counter_all': 7216},
    {'UID': 462627, 'NAME': 'Ibelin', 'PASS': '272646', 'GENRE': '0', 'counter': '0', 'charges': 999987,
     'counter_all': 13},
    {'UID': 5558083, 'NAME': 'PrincessYukino', 'PASS': '2515723', 'GENRE': '0', 'counter': '0', 'charges': 1000000,
     'counter_all': 0},
    {'UID': 2968993, 'NAME': 'Yosu', 'PASS': '237152', 'GENRE': '0', 'counter': '0', 'charges': 1000000,
     'counter_all': 0},
    {'UID': 5603968, 'NAME': 'Nasa', 'PASS': '521237', 'GENRE': '0', 'counter': '0', 'charges': 999999,
     'counter_all': 1},
    {'UID': 4859831, 'NAME': 'a1', 'PASS': '593181', 'GENRE': '0', 'counter': '0', 'charges': 0, 'counter_all': 1000},
    {'UID': 3238595, 'NAME': 'daobujing', 'PASS': '333666', 'GENRE': '0', 'counter': '1955', 'charges': 2431,
     'counter_all': 8964}]


class User():
    def __init__(self, uid, name, password, genre, counter, charges, counter_all):
        self.uid = uid
        self.name = name
        self.password = password
        self.genre = genre
        self.charges = charges
        self.counter = counter
        self.counter_all = counter_all


sqlite.create_db()
for i in data:
    i2 = User(i["UID"], i["NAME"], i["PASS"], i["GENRE"], i["counter"], i["charges"], i["counter_all"])
    sqlite.user_add(i2)
