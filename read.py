import pymysql
import pandas as pd
import DB
# 打开数据库连接
conn=pymysql.connect(host='localhost',port=3306,user='root',password='123456',charset='utf8',db='student')
df = pd.read_sql('SELECT * FROM student.class1 order by que',con=conn)
#print(df)

id=df.id.values
que=df.que.values
name=df.name.values
situation=df.attendance.values
score=df.score.values
for i in situation:
    print(i)


# 关闭数据库连接
conn.close()