import random
import pymysql
import numpy as np
import read
conn=pymysql.connect(host='localhost',port=3306,user='root',password='123456',charset='utf8',db='student')
cursor = conn.cursor()
for num in range(1,6):
    plansname = "plans" + str(num)
    sql1 = """drop table if exists %s""" % plansname
    sql2 = """
            create table %s(
            id int,
            name varchar(20),
            pl varchar(20)
            )
            """ % plansname
    cursor.execute(sql1)
    cursor.execute(sql2)
    conn.commit()
conn.close()


def output(plans,plan):
    for i in range(1,91):
        for j in range(90):
            if(read.id[j]==i):
                conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', charset='utf8',db='student')
                cursor = conn.cursor()
                sql3 = """insert into %s(id,name,pl) values ('%d','%s','%s')""" % (plans,read.id[j],read.name[j],plan[j])
                cursor.execute(sql3)
                conn.commit()
                conn.close()


