import pymysql
import numpy as np
import DB
def read_data(tablename):
    global id
    global que
    global name
    global situation
    global score
    # 打开数据库连接
    conn=pymysql.connect(host='localhost',port=3306,user='root',password='123456',charset='utf8',db='student')

    cursor = conn.cursor()
    cursor.execute("select id from %s order by que"% tablename)
    l1=cursor.fetchall()
    id=[i[0] for i in l1]
    cursor.execute("select que from %s order by que"% tablename)
    l2=cursor.fetchall()
    que=[i[0] for i in l2]
    cursor.execute("select name from %s order by que"% tablename)
    l3=cursor.fetchall()
    name=[i[0] for i in l3]
    cursor.execute("select attendance from %s order by que"% tablename)
    l4=cursor.fetchall()
    situation=[i[0] for i in l4]
    cursor.execute("select score from %s order by que"% tablename)
    l5=cursor.fetchall()
    score=[i[0] for i in l5]

    # 关闭数据库连接
    conn.close()
#