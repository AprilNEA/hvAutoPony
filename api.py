#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @author: Green Sulley
# @license: AGPL-3.0 License
# @contact: sukeycz0@gmail.com
# @software: PyCharm
# @project : hvAutoPony
# @file: api.py
# @time: 2021/6/4 22:54
# @desc:
import re
import yaml

import requests
import uvicorn

from pydantic import BaseModel

from fastapi import FastAPI, Request

import main

app = FastAPI()

allow_uid = []
IF_CHECK_UID = True
IF_CHECK_PONY = False

with open("allow_uid.txt") as f:
    lines = f.readlines()
    for line in lines:
        allow_uid.append(int(line.replace('\n', '')))

with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)


@app.get("/")
def read_root():
    return "AutoPony Server is working!"


class Info(BaseModel):
    base64Data: str
    img_src: str


def check_pony(user_id: int, ponyimg_token: str) -> bool:
    url = f"http://alt.hentaiverse.org/riddlemaster?uid={user_id}&v={ponyimg_token}"
    session = requests.Session()
    response = session.get(url=url)
    if response.text == "Riddle mismatch":
        return False
    else:
        return True


@app.post("/autopony/")
def get_riddle_answer(info: Info, request: Request):
    if IF_CHECK_UID:
        if "hentaiverse.org" in info.img_src:
            src = re.findall(r'uid=([a-zA-Z0-9]+)&v=([a-zA-Z0-9]+)',
                             info.img_src)
            uid = src[0]
            token = src[1]
            if IF_CHECK_PONY:
                if check_pony(uid, token):
                    authority = True
                else:
                    authority = False
            else:
                if uid in allow_uid:
                    authority = True
                else:
                    authority = False
        elif "ponytest.pages.dev" in info.img_src:
            authority = True
        else:
            authority = False
    else:
        authority = True
    if authority:
        answer, pony = main.autopony(info.base64Data)
        back = {"code": 0, "return": {"answer": answer, "pony": pony}}
        return back
    else:
        return {"code": 1}


@app.get("/autopony/{key}/user/{stype}/{uid}")
def useroperate(key: str, stype: str, uid: int):
    if key != config["key"]:
        return {"Wrong": "Permission error"}
    if stype == "add":
        if uid in allow_uid:
            return {"User Add": "Already exists"}
        else:
            allow_uid.append(uid)
            with open("allow_uid.txt", "a") as f:
                f.writelines(str(uid) + "\n")
            return {"User Add": "Success"}
    if stype == "detele":
        if uid not in allow_uid:
            return {"User detele": "User does not exist"}
        else:
            allow_uid.remove(uid)
            return {"User detele": "Success"}


if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=9002, log_level="debug")
