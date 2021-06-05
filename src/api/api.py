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
import uvicorn

from db import sqlite
from src.lib.assort.assort import autopony
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


class Info(BaseModel):
    password: str
    base64Data: str
    user_id: int
    ponyimg_token: int


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.post("/pony/api/post/{uid}/")
def main(uid: int, info: Info):
    exist = sqlite.user_exist(uid, info.password)
    if exist:
        print(exist)
        name, genre, counter, charges, counter_all = exist[1], exist[3], exist[4], exist[5], exist[6]
        # genre 0代表永久 1代表按量付费 2代表按时间
        if genre == 0:
            answer, pony = autopony(info.base64Data)
            sqlite.update(uid, "counter", counter + 1)
            sqlite.update(uid, "counter_all", counter_all + 1)
            back = {
                "name": name,
                "answer": answer,
                "pony": pony,
                "counter": counter,
                "counter_all": counter_all,
            }
            return {"code": 0, "genre": 0, "return": back}
        elif genre == 1:
            if charges > 0:
                answer, pony = autopony(info.base64Data)
                sqlite.update(uid, counter, counter + 1)
                sqlite.update(uid, charges, charges - 1)
                sqlite.update(uid, counter_all, counter_all + 1)
                back = {
                    "name": name,
                    "answer": answer,
                    "pony": pony,
                    "counter": counter,
                    "charges": charges,
                    "counter_all": counter_all,
                }
                return {"code": 0, "genre": 1, "return": back}
            else:
                return {"code": 1}
        elif genre == 2:
            pass
    elif exist == 3:
        return 3
    else:
        return


if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=5000, log_level="info")
