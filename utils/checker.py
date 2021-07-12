#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @author: sukeycz
# @license:
# @contact: sukeycz0@gmail.com
# @software: PyCharm
# @project : hvAutoPony
# @file: checker.py
# @time: 2021/6/6 15:19
# @desc:
import os
import settings
import requests



def pony_exists(uid, img_token):
    url = f"http://alt.hentaiverse.org/riddlemaster?uid={uid}&v={img_token}"
    session = requests.Session()
    response = session.get(url=url)
    if response.text == "Riddle mismatch":
        return False
    else:
        return True



if __name__ == '__main__':
    uid = ""
    token = ""
    pony_exists(uid, token)
