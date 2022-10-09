import numpy as np
import random
Convict=random.randint(5,8)#生成随机数，选择要查询多少人
print(Convict)
prisoner=random.sample(range(71,91),Convict)#这个数组是问题学生
print(prisoner)
situation = np.array(['11111111111111111111' for _ in range(90)], dtype=object)#到勤情况

for i in prisoner:
    ran = random.sample(range(1, 91), 90)
    nums = ['1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
    np.random.shuffle(nums)
    salt = ''.join(nums)
    situation[i-1]=salt


#二十节课，每节请假的人，如果不在要查询的人里面则这节课的到勤情况设置为0
for i in range(20):
    innocent=random.randint(0,3)
    #print(innocent)
    goodguy=random.sample(range(1,91),innocent)#请假的人的序号
    #print(goodguy)
    for j in goodguy:
        if j not in prisoner:
            s=situation[j-1]
            t = list(s)
            t[i] = '0'
            s = ''.join(t)
            situation[j-1]=s
print(situation)

def limit(num):
    if num>4:
        return 4
    if num<0:
        return 0

    return num


x=[]
for i in range(90):
    a=np.random.normal(loc=2.8, scale=0.5, size=None)
    b=limit(a)
    c=round(b,2)
    x.append(c)
x.sort(reverse=True)
print(x)
e = np.array(['00000000000000000000' for _ in range(70)], dtype=object)
f = np.array(['11000000000000000000' for _ in range(20)], dtype=object)
g = [e,f]
m = tuple(g)
plan = np.hstack(m)
badguy=[]
for i in range(70,90):
    if situation[i][0]!=plan[i][0] or situation[i][1]!=plan[i][1]:
        badguy.append(i+1)
        plan[i]='11111111111111111111'

for i in badguy:
    if situation[i-1][2]=='1' and situation[i-1][3]=='1' and situation[i-1][4]=='1':
        sh = plan[i-1]
        temp = list(sh)
        for j in range(5,20):
            temp[j] = '0'
        sh = ''.join(temp)
        plan[i-1] = sh

number=0
for i in range(70,90):
    for j in range(0,20):
        da = plan[i]
        mo = situation[i]
        dad=list(da)
        mom=list(mo)
        if dad[j]=='1' and mom[j] == '0':
            number = number +1
print(number)

total=40
for i in range(70,90):
    for j in range(2,20):
        if plan[i][j] == '1':
            total = total + 1
print(total)
print(plan)
print(badguy)
print(number/total)
#