import sqlite3


def add(uid, name, password, genre, time, timesleft, timesall):
    conn = sqlite3.connect('pony.db')
    c = conn.cursor()
    sql = "INSERT INTO USERPONY (UID,NAME,PASS,GENRE,TIME,TIMESLEFT,TIMESALL) \
          VALUES (" + uid + ", '" + name + "','" + password + "','" + genre + "','" + time + "'," + timesleft + "," + timesall + ")"
    c.execute(sql)
    conn.commit()
    print('Records created successfully')
    conn.close()


add('5098427', 'yama', '225500', '0', '0', '2857', '0')
