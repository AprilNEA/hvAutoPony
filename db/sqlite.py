#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @author: sukeycz
# @license:
# @contact: sukeycz0@gmail.com
# @software: PyCharm
# @project : hvAutoPony
# @file: sqlite.py
# @time: 2021/6/5 19:40
# @desc:

import sqlite3

DB_ADDRESS = "pony.db"
USERTABLE_NAME = "USERPONY"


def create_db():
    import sqlite3

    conn = sqlite3.connect(DB_ADDRESS)
    c = conn.cursor()
    c.execute('''CREATE TABLE USERPONY
           (
               UID INT PRIMARY KEY NOT NULL,
               NAME TEXT NOT NULL,
               PASS  TEXT NOT NULL,
               GENRE INT NOT NULL,
               counter INT,
               charges INT,
               counter_all INT
           );
           ''')
    print("Table created successfully")
    conn.commit()
    c.execute('''CREATE TABLE USERLOG
               (
                    ID INTEGER PRIMARY KEY,
                    UID INT NOT NULL,
                    NAME TEXT NOT NULL,
                    IP TEXT NOT NULL,
                    REAL_UID INT NOT NULL
               );
               ''')
    conn.commit()
    conn.close()
    print("Opened database successfully")


def user_add(user):
    """
    :param user: class:
                    uid: int
                    name: str
                    password: str
                    genre: int # 0代表永久 1代表按量付费 2代表按时间
                    counter: int
                    charges: int
                    counter_all: int
    :return: True or False
    """
    conn = sqlite3.connect(DB_ADDRESS)
    c = conn.cursor()
    sql = f'INSERT INTO USERPONY (UID,NAME,PASS,GENRE,counter,charges,counter_all) VALUES ({user.uid},"{user.name}","{user.password}",{user.genre},{user.counter},{user.charges},{user.counter_all})'
    print(sql)
    c.execute(sql)
    conn.commit()
    print('Records created successfully')
    conn.close()


def user_exist(uid, password):
    conn = sqlite3.connect("D:\Github\hvAutoPony\db\pony.db")
    c = conn.cursor()
    sql = f"SELECT * from USERPONY where UID = {uid}"
    c.execute(sql)
    # * = UID,NAME,PASS,GENRE,counter,charges,counter_all
    result = c.fetchone()
    if result:
        if password == result[2]:
            return result
        else:
            return 3 # 密码错误
    else:
        return False



def user_delete(uid):
    conn = sqlite3.connect(DB_ADDRESS)
    c = conn.cursor()
    print("Opened database successfully")
    sql = f"DELETE from {USERTABLE_NAME} where UID={uid};"
    c.execute(sql)
    conn.commit()
    print("Total number of rows deleted :", conn.total_changes)
    print("Operation done successfully")
    conn.close()


def update(uid, which, key):
    conn = sqlite3.connect(DB_ADDRESS)
    c = conn.cursor()
    print("Opened database successfully")
    sql = f"UPDATE USERPONY set {which}= {key} where UID= {uid}"
    print(sql)
    c.execute(sql)
    conn.commit()
    print("Total number of rows updated :" + str(conn.total_changes))
    conn.close()

