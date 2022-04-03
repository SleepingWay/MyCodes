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
    for i in range(100):
        result.append(miller_rabin(p))
    percent = result.count(True) / len(result)
    if percent > 0.8:
        return p


# if __name__ == '__main__':
#     p = int(input("请输入需要判断的数字:"))
    # result = []
    # for i in range(10):
    #     result.append(miller_rabin(p))
    # print(result)
    # print(result.count(True) / len(result))
