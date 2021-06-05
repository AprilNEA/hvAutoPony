#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @author: sukeycz
# @license:
# @contact: sukeycz0@gmail.com
# @software: PyCharm
# @project : hvAutoPony
# @file: testing.py
# @time: 2021/6/5 21:30
# @desc:
import requests
import base64

img_src = 'https://ponytest.pages.dev/pony1000/573.jpg'
img = requests.get(img_src)
base64Data = base64.b64encode(img.content).decode('utf-8')
r = requests.post(url="http://127.0.0.1:5000/pony/api/post/0/", json={
    "password": "781898",
    "base64Data": base64Data,
    "user_id": 1,
    "ponyimg_token": 1,
})
print(r.text)
