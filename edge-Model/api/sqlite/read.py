import sqlite3

conn = sqlite3.connect('pony.db')
c = conn.cursor()
print ("Opened database successfully")

cursor = c.execute("SELECT UID,NAME,PASS,GENRE,TIME,TIMESLEFT,TIMESALL  from USERPONY")
for row in cursor:
   print ("UID = " + str(row[0]))
   print ("NAME = " + str(row[1]))
   print ("PASS = " + str(row[2]))
   print ("GENRE = "+ str(row[3]))
   print ("TIME = "+ str(row[4]))
   print("TIMESLEFT = " + str(row[5]))
   print("TIMESALL = " + str(row[6]))

print ("Operation done successfully")
conn.close()