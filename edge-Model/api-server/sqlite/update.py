import sqlite3
def update(uid,which,key):
    conn = sqlite3.connect('pony.db')
    c = conn.cursor()
    print("Opened database successfully")
    sql = "UPDATE USERPONY set " + which +" = " + key + " where " + "UID=" + uid
    print(sql)
    c.execute(sql)
    conn.commit()
    print("Total number of rows updated :" + str(conn.total_changes))
    conn.close()
update()
