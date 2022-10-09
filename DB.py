import pymysql
import random

# 打开数据库连接
conn=pymysql.connect(host='localhost',port=3306,user='root',password='123456',charset='utf8',db='student')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()

#cursor.execute("create database student")
#conn.commit()

#cursor.execute("show databases")
# 使用 fetchone() 方法获取单条数据.
#result = cursor.fetchall()
#print(result)
#sql1 = """drop table if exists class1"""
#cursor.execute(sql1)
#cursor.execute("use student")
sql1 = """drop table if exists class1"""
sql2="""
create table class1(
    que int not null auto_increment primary key,
    id int,
    attendance varchar(20),
    sampling varchar(20),
    cnt int
)
"""
cursor.execute(sql1)
cursor.execute(sql2)
conn.commit()
#rank int auto_increment primary key,
ran = random.sample(range(1, 91), 90)

for i in ran:
    sql3 = "insert into class1(id) values ('%s')" %(i)
    cursor.execute(sql3)
    conn.commit()


# 关闭数据库连接
#cursor.execute("drop table class1")
#conn.commit()

#cursor.execute("drop database student")
#conn.commit()
cursor.close()
conn.close()
