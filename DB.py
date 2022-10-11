import pymysql
import random
from faker import Faker
import create_data

create_data.create()

conn=pymysql.connect(host='localhost',port=3306,user='root',password='123456',charset='utf8',db='student')

cursor = conn.cursor()

sql1 = """drop table if exists class1"""
sql2="""
create table class1(
    id int not null auto_increment primary key,
    que int,
    name varchar(20),
    attendance varchar(20),
    score float
)
"""
cursor.execute(sql1)
cursor.execute(sql2)
conn.commit()

ran = random.sample(range(1, 91), 90)

faker = Faker('zh_CN')
for i in ran:
    sql3 = "insert into class1(que,name,attendance,score) values ('%d','%s','%s','%f')" % (i,faker.name(),create_data.situation[i-1],create_data.x[i-1])
    cursor.execute(sql3)
    conn.commit()

cursor.close()
conn.close()
