#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @author: sukeycz
# @license:
# @contact: sukeycz0@gmail.com
# @software: PyCharm
# @project : hvAutoPony
# @file: api.py
# @time: 2021/6/4 22:54
# @desc:
import os
import settings

import re
import time
import json
import random
import uvicorn

from db import sqlite
from utils import checker, logger, assort

from typing import Optional
from pydantic import BaseModel

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
def read_root():
    return {"Hello": "World"}


class Info(BaseModel):
    password: str
    base64Data: str
    img_src: str


def check_pony(user_id, ponyimg_token):
    return checker.pony_exists(user_id, ponyimg_token)


class User():
    def __init__(self, exist):
        self.uid = exist[0]
        self.name = exist[1]
        self.password = exist[2]
        self.genre = exist[3]
        self.charges = exist[4]
        self.counter = exist[5]
        self.counter_all = exist[6]
        self.ip = None
        self.real_uid = None
        self.answer = None
        self.pony = None

    def use_pony(self):
        sqlite.update(self.uid, "counter", self.counter + 1)
        sqlite.update(self.uid, "counter_all", self.counter_all + 1)
        if self.genre == 1:
            if not sqlite.update(self.uid, "charges", self.charges - 1):
                pass  # 错误日志

    def logging(self, ip, real_uid, option, pony):
        self.ip = ip
        self.real_uid = real_uid
        self.option = option
        self.pony = pony
        logger.logger(self)
        sqlite.log_add(self)


# @app.get("/ponytest/")
# def send_testpony_token(token: Optional[str] = None):
#     if not token:
#         token_new = ''.join(random.sample('0123456789zyxwvutsrqponmlkjihgfedcba', 7))
#         with open(settings.PublicDirectory, "pony_img/token.json", "r+w") as f:
#             if f:
#                 token_all = json.load(f)
#                 for token, time_add in token_all.item():
#                     time_now = time.gmtime()
#                     if time_add - time_now >= 20:
#                         del token_all[token]
#                 token_all.append({token_new: time.gmtime()})
#         url = f"http://127.0.0.1:5001/ponytest/?token={token}"
#         return {"url": url}
#     else:
#         with open(settings.PublicDirectory, "pony_img/token.json", "r+w") as f:
#             if token in f:
#                 token_all = json.load(f)
#                 del token_all[token]
#                 f.write(json.dumps(token_all))
#                 return FileResponse(os.path.join(settings.PublicDirectory,
#                                                  f"pony_img/pony1000/{random.randint(1, 1000)}.jpg"))
#             else:
#                 pass


@app.get("/pony/script/{uid}/{password}", response_class=HTMLResponse)
def get_script(request: Request, uid: int, password: str):
    if sqlite.user_exist(uid, password):
        return templates.TemplateResponse("script.html", {"request": request, "uid": uid, "password": password})
    else:
        return {"return": "权限错误"}


@app.post("/pony/api/post/{uid}/")
def get_riddle_answer(uid: int, info: Info, request: Request):
    # print(info)
    # UID,NAME,PASS,GENRE,counter,charges,counter_all
    exist = sqlite.user_exist(uid, info.password)
    if exist:
        user = User(exist)
        print(info.img_src)
        if "hentaiverse.org" in info.img_src:
            src = re.findall(r'uid=([a-zA-Z0-9]+)&v=([a-zA-Z0-9]+)', info.img_src)
            user_id = src[0]
            ponyimg_token = [1]
        else:
            user_id = uid
            # check_pony(user_id, ponyimg_token)
        # if not check_pony():
        #     pass
        user.use_pony()
        # genre 0代表永久 1代表按量付费 2代表按时间
        if user.genre == 0:
            answer, pony = assort.autopony(info.base64Data)
            back = {
                "code": 0,
                "genre": 0,
                "return": {
                    "name": user.name,
                    "answer": answer,
                    "pony": pony,
                    "counter": user.counter,
                    "counter_all": user.counter_all,
                }
            }
        elif user.genre == 1:
            # 检查存量是否充足
            if user.charges > 0:
                answer, pony = assort.autopony(info.base64Data)
                back = {
                    "code": 0,
                    "user.genre": 1,
                    "return": {
                        "name": user.name,
                        "answer": answer,
                        "pony": pony,
                        "counter": user.counter,
                        "charges": user.charges,
                        "counter_all": user.counter_all,
                    }
                }
            else:
                return {"code": 1}
        else:
            return {"code": 1}
        user.logging(request.client.host, user_id, answer, pony)
        return back
    else:
        return {"code": 2}


if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=5001, log_level="info")
