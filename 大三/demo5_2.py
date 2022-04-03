import random


def miller_rabin(p: int) -> bool:
    if p == 2:  # 输入为2时直接返回是素数
        return True
    elif p & 1 == 0:  # 输入为偶数时直接返回不是素数
        return False
    else:  # 当输入为奇数时进入
        a = random.randint(2, p - 2)  # 获取一个随机数a
        k = 0
        tmp = p - 1
        while True:  # 求 k 和 m
            if tmp % 2 == 0:
                tmp = int(tmp / 2)
                k += 1
            else:
                break
        m = tmp
        tmp1 = (a ** m) % p
        if tmp1 == 1:
            return False
        for i in range(k - 1):  # 使用二次探测定理进行素性判断
            tmp2 = tmp1
            tmp1 = (tmp1 ** 2) % p
            if tmp2 != 1 and tmp2 != p - 1 and tmp1 == 1:
                return False
        tmp1 = (tmp1 ** 2) % p  # 使用Fermat定理进行最后的判断
        if tmp1 == 1:
            return True
        else:
            return False


def resJudge(p):
    result = []
    for i in range(10):
        result.append(miller_rabin(p))
    percent = result.count(True) / len(result)
    if percent > 0.5:
        return p


def chooseNum():  # 选择Alice的大素数
    Pa = 0
    a = random.randint(1000, 5000)
    for i in range(a, 10000):
        if Pa == 0 or Pa is None:
            Pa = resJudge(i)
        else:
            break
    return Pa


def primitiveRoot(num):  # 求本原根
    flag = True
    while True:
        root = random.randint(2, num - 1)
        for i in range(1, num):
            if pow(root, i, num) == 1 and i != num - 1:
                flag = False
                break
        if flag:
            break
    return root


def AliceWriteM(m):
    p = chooseNum()
    g = primitiveRoot(p)
    x = random.randint(1, p - 1)
    y = pow(g, x, p)
    '''Alice签署消息m'''
    k = random.randint(1, int(p ** (1 / 2)))
    k_1, k_2 = ext_gcd(k, p - 1)
    r = pow(g, k, p)
    s = (pow(k_1, 1, p - 1) * pow(m - x * r, 1, p - 1)) % (p - 1)
    return p, g, y, r, s


def BobConfirm(p, g, y, m, r, s):
    v1 = (pow(y, r, p) * pow(r, s, p)) % p
    v2 = pow(g, m, p)
    print('v1 = {}\nv2 = {}'.format(v1, v2))
    if v1 == v2:
        print('签名有效')
    else:
        print('签名无效')


def ext_gcd(a, b):
    if b == 0:
        return 1, 0
    else:
        x, y = ext_gcd(b, a % b)
        x, y = y, (x - (a // b) * y)
        return x, y


if __name__ == '__main__':
    message = 1914008
    print(message)
    P, G, Y, R, S = AliceWriteM(message)
    BobConfirm(P, G, Y, message, R, S)
