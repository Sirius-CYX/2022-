import pymysql
import random
from faker import Faker
import create_data



conn=pymysql.connect(host='localhost',port=3306,user='root',password='123456',charset='utf8',db='student')

cursor = conn.cursor()
for num in range(1,6):
    create_data.create()
    tablename = "class" + str(num)
    sql1 = """drop table if exists %s""" % tablename
    sql2="""
    create table %s(
        id int not null auto_increment primary key,
        que int,
        name varchar(20),
        attendance varchar(20),
        score float
    )
    """ % tablename
    cursor.execute(sql1)
    cursor.execute(sql2)
    conn.commit()

    ran = random.sample(range(1, 91), 90)

    faker = Faker('zh_CN')
    for i in ran:
        sql3 = "insert into %s(que,name,attendance,score) values ('%d','%s','%s','%f')" % (tablename,i,faker.name(),create_data.situation[i-1],create_data.x[i-1])
        cursor.execute(sql3)
        conn.commit()

cursor.close()
conn.close()
#