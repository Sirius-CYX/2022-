import numpy as np
import random
import read

e = np.array(['00000000000000000000' for _ in range(70)], dtype=object)
f = np.array(['11000000000000000000' for _ in range(20)], dtype=object)
g = [e,f]
m = tuple(g)
plan = np.hstack(m)
badguy=[]
for i in range(70,90):
    if read.situation[i][0]!=plan[i][0] or read.situation[i][1]!=plan[i][1]:
        badguy.append(i+1)
        plan[i]='11111111111111111111'

for i in badguy:
    if read.situation[i-1][2]=='1' and read.situation[i-1][3]=='1' and read.situation[i-1][4]=='1':
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
        mo = read.situation[i]
        dad=list(da)
        mom=list(mo)
        if dad[j]=='1' and mom[j] == '0':
            number = number +1


total=40
for i in range(70,90):
    for j in range(2,20):
        if plan[i][j] == '1':
            total = total + 1

print(read.situation)
print(plan)
print(number)
print(total)
print(badguy)
print(number/total)
#