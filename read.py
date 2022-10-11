import pymysql
import DB
# 打开数据库连接
conn=pymysql.connect(host='localhost',port=3306,user='root',password='123456',charset='utf8',db='student')

cursor = conn.cursor()
cursor.execute("select id from class1 order by que")
l1=cursor.fetchall()
id=[i[0] for i in l1]
cursor.execute("select que from class1 order by que")
l2=cursor.fetchall()
que=[i[0] for i in l2]
cursor.execute("select name from class1 order by que")
l3=cursor.fetchall()
name=[i[0] for i in l3]
cursor.execute("select attendance from class1 order by que")
l4=cursor.fetchall()
situation=[i[0] for i in l4]
cursor.execute("select score from class1 order by que")
l5=cursor.fetchall()
score=[i[0] for i in l5]


# 关闭数据库连接
conn.close()