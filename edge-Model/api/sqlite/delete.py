import sqlite3
def delete(uid):
    conn = sqlite3.connect('pony.db')
    c = conn.cursor()
    print("Opened database successfully")
    sql = "DELETE from USERPONY where UID="+uid+";"
    c.execute(sql)
    conn.commit()
    print("Total number of rows deleted :", conn.total_changes)
    print("Operation done successfully")
    conn.close()