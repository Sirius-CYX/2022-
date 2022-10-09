import numpy as np
import random
Convict=random.randint(5,8)
print(Convict)
prisoner=random.sample(range(71,91),Convict)
print(prisoner)
situation = np.array(['11111111111111111111' for _ in range(90)], dtype=object)

for i in prisoner:
    ran = random.sample(range(1, 91), 90)
    nums = ['1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
    np.random.shuffle(nums)
    salt = ''.join(nums)
    situation[i-1]=salt


for i in range(20):
    innocent=random.randint(0,3)
    print(innocent)
    goodguy=random.sample(range(1,91),innocent)
    print(goodguy)
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

print(plan)
print(badguy)
total=40
for i in range(70,90):
    for j in range(2,20):
        if plan[i][j] == plan[i][1]:
            total = total + 1
print(total)