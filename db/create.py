import sqlite3

conn = sqlite3.connect('pony.db')
c = conn.cursor()
c.execute('''CREATE TABLE USERPONY
       (UID INT PRIMARY KEY   NOT NULL,
       NAME           TEXT,
       PASS           TEXT    NOT NULL,
       GENRE          TEXT,
       TIME           TEXT,
       TIMESLEFT      INT,
       TIMESALL       INT
       );''')
print("Table created successfully")
conn.commit()
conn.close()
print("Opened database successfully")
