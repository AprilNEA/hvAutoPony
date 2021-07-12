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
import os
import settings
import sqlite3

DB_ADDRESS = "db/pony.db"
USERTABLE_NAME = "USERPONY"


def create_db():
    try:
        conn = sqlite3.connect(DB_ADDRESS)
    except sqlite3.DatabaseError:
        print("数据库连接错误")
        return False

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
    :param user(class)
    uid: int
    name: str
    password: str
    genre: int # 0代表永久 1代表按量付费 2代表按时间
    counter: int
    charges: int
    counter_all: int
    :return: True or False
    """
    try:
        conn = sqlite3.connect(DB_ADDRESS)
    except sqlite3.DatabaseError:
        print("数据库连接错误")
        return False
    try:
        c = conn.cursor()
        sql = f'INSERT INTO USERPONY (UID,NAME,PASS,GENRE,counter,charges,counter_all) VALUES ({user.uid},"{user.name}","{user.password}",{user.genre},{user.counter},{user.charges},{user.counter_all})'
        c.execute(sql)
        conn.commit()
    except sqlite3.ProgrammingError:
        print("SQL语句错误")
        return False
    else:
        print("用户添加成功")
        return True
    conn.close()


def user_exist(uid, password):
    try:
        conn = sqlite3.connect(DB_ADDRESS)
    except sqlite3.DatabaseError:
        print("检查用户是否存在时数据库连接错误")
        return False
    try:
        c = conn.cursor()
        sql = f"SELECT * from USERPONY where UID = {uid}"
        c.execute(sql)
        # * = UID,NAME,PASS,GENRE,counter,charges,counter_all
        result = c.fetchone()
    except sqlite3.ProgrammingError:
        print("SQL语句错误")
        return False
    else:
        if result:
            if password == result[2]:
                return result
            else:
                return False
        else:
            return False


def user_delete(uid):
    try:
        conn = sqlite3.connect(DB_ADDRESS)
    except sqlite3.DatabaseError:
        print("数据库连接错误")
        return False
    try:
        c = conn.cursor()
        sql = f"DELETE from {USERTABLE_NAME} where UID={uid};"
        c.execute(sql)
        conn.commit()
    except sqlite3.ProgrammingError:
        print("用户删除失败")
        return False
    conn.close()
    return True


def update(uid, which, key):
    """
    :param uid: 数据库主键
    :param which: 栏目
    :param key: 值
    :return:
    """
    try:
        conn = sqlite3.connect(DB_ADDRESS)
    except sqlite3.DatabaseError:
        print("数据库连接错误")
        return False
    try:
        c = conn.cursor()
        sql = f"UPDATE USERPONY set {which}= {key} where UID= {uid}"
        c.execute(sql)
        conn.commit()
    except sqlite3.ProgrammingError:
        print("数据库更新失败")
        return False
    conn.close()
    return True


def log_add(log):
    """
    记录用户UID及真实IP地址
    :param log:
    UID INT NOT NULL,
    NAME TEXT NOT NULL,
    IP TEXT NOT NULL,
    REAL_UID INT NOT NULL
    :return:
    """
    try:
        conn = sqlite3.connect(DB_ADDRESS)
    except sqlite3.DatabaseError:
        print("数据库连接错误")
        return False
    try:
        c = conn.cursor()
        sql = f"SELECT IP,REAL_UID from USERLOG where UID = {log.uid}"
        c.execute(sql)
    except sqlite3.ProgrammingError:
        print("SQL语句错误")
        return False
    else:
        results = c.fetchall()
        if results:
            for result in results:
                if not log.real_uid == result[1] and log.ip == result[0]:
                    try:
                        c = conn.cursor()
                        sql = f'INSERT INTO USERLOG (UID,NAME,IP,REAL_UID) VALUES ({log.uid},"{log.name}","{log.ip}",{log.real_uid})'
                        c.execute(sql)
                        conn.commit()
                    except sqlite3.ProgrammingError:
                        print("SQL语句错误")
                        return False
                    else:
                        print("日志添加成功")
                        return True
    conn.close()


if __name__ == '__main__':
    # print(DB_ADDRESS)
    user_add()
