import numpy as np
import random

def random_create():
    Convict = random.randint(5, 8)  # 生成随机数
    prisoner = random.sample(range(71, 91), Convict)  # 这个数组是问题学生
    situation = np.array(['11111111111111111111' for _ in range(90)], dtype=object)  # 到勤情况

    for i in prisoner:
        ran = random.sample(range(1, 91), 90)
        nums = ['1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
        np.random.shuffle(nums)
        salt = ''.join(nums)
        situation[i - 1] = salt

        for i in range(20):
            innocent = random.randint(0, 3)
            goodguy = random.sample(range(1, 91), innocent)  # 请假的人的序号
            for j in goodguy:
                if j not in prisoner:
                    s = situation[j - 1]
                    t = list(s)
                    t[i] = '0'
                    s = ''.join(t)
                    situation[j - 1] = s

        def limit(num):
            if num > 4:
                return 4
            if num < 0:
                return 0

            return num

        x = []
        for i in range(90):
            a = np.random.normal(loc=2.8, scale=0.5, size=None)
            b = limit(a)
            c = round(b, 2)
            x.append(c)
        x.sort(reverse=True)

random_create()