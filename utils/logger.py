#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @author: sukeycz
# @license:
# @contact: sukeycz0@gmail.com
# @software: PyCharm
# @project : hvAutoPony
# @file: logger.py
# @time: 2021/6/6 15:22
# @desc:
import os
import time
import json

def logger(user):
    log = json.dumps({
        "time": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()),
        "user": {
            "uid": user.uid,
            "name": user.name,
            "genre": user.genre,
            "ip": user.ip,
            "real_uid": user.real_uid
        },
        "pony": {
            "counter": user.counter,
            "counter_all": user.counter_all,
            "charges": user.charges,
            "answer": user.option,
            "pony": user.pony
        }
    })
    if not os.path.exists(f"archivelog/{user.uid}"):
        os.makedirs(f"archivelog/{user.uid}")
    filename = f'archivelog/{user.uid}/{time.strftime("%Y-%m-%d", time.gmtime())}.json'
    try:
        with open(filename, 'a+', encoding='utf-8') as f:
            f.write(log + ',\n')
        return True
    except IOError as err:
        print("文件处理错误:" + str(err))
        return False

