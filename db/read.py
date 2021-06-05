import sqlite3

conn = sqlite3.connect('pony.db')
c = conn.cursor()
print("Opened database successfully")
b = []
# cursor = c.execute("SELECT UID,NAME,PASS,GENRE,TIME,TIMESLEFT,TIMESALL from USERPONY")
cursor = c.execute("SELECT * from USERPONY")
for row in cursor:
   a = {
      "UID": row[0],
      "NAME": row[1],
      "PASS": row[2],
      "GENRE": row[3],
      "counter":row[4],
      "charges": row[5],
      "counter_all": row[6]
   }
   b.append(a)
print(b)
