import datetime
import sqlite3


def doSth():
    conn = sqlite3.connect('sqlite/pony.db')
    c = conn.cursor()
    cursor = c.execute("SELECT UID,PASS,NAME,GENRE,TIME,TIMESLEFT,TIMESALL from USERPONY")
    for row in cursor:
        sql = "UPDATE USERPONY set " + "TIME" + " = 0 where " + "UID=" + str(row[0])
        c.execute(sql)
        conn.commit()
    conn.close()

def main(h=0, m=0):
    while True:
        while True:
            now = datetime.datetime.now()
            print(str(now) + " Checked")
            if now.hour == h: #and now.minute == m:
                break
            time.sleep(3500)
        doSth()
if __name__ == '__main__':
    main()
