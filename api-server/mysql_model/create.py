import mysql.connector

mydb = mysql.connector.connect(
    host="hk.sukeycz.com",  # 数据库主机地址
    user="autopony",  # 数据库用户名
    passwd="DPzzDhx5NcYGezHR", # 数据库密码
    database="autopony"
)

print(mydb)

mycursor = mydb.cursor()
#mycursor.execute("ALTER TABLE users ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

sql = "INSERT INTO users (uid, username, password) VALUES (%s, %s, %s)"
val = 0

for i in val:
    mycursor.execute(sql, i)

mydb.commit()  # 数据表内容有更新，必须使用到该语句

print(mycursor.rowcount, "记录插入成功。")

