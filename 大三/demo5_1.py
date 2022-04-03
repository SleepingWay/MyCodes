import math
import random as ran


def ext_gcd(a, b):
    if b == 0:
        return 1, 0
    else:
        x, y = ext_gcd(b, a % b)
        x, y = y, (x - (a // b) * y)
        return x, y


def cal(a, b, p, i):
    hashmap1, hashmap2 = {}, {}
    for j in range(math.floor(p ** (1 / 2))):
        k = ran.randint(1, p - 1)
        l = ran.randint(1, p - 1)
        hashmap1[pow(a, k, p)] = k
        a_1, a_2 = ext_gcd(a, p)    # 求α的逆
        hashmap2[(b * a_1) % p] = l
    res = 0
    for x in hashmap1.keys():
        if x in hashmap2.keys():
            res = hashmap1[x] + hashmap2[x]
            break
    if res != 0:
        print(i, '离散对数为 : {}'.format(res))
    else:
        print(i, '本次运算没有得出结果')
    # print(hashmap1, hashmap2)


a = int(input('输入本原根:'))
b = int(input('输入本原根的某一阶:'))
p = int(input('输入大素数:'))
for i in range(10000):
    cal(a, b, p, i)

