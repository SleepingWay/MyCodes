from functools import reduce
import random as ran


def numAdd():
    a = input('任意自然数：')
    sum = 0
    for i in a:
        sum += int(i)
    print(f'{a}的各位之和为:{sum}')


def setAdd():
    a = eval(input('输入{集合a}:'))
    b = eval(input('输入{集合b}:'))
    print(f'{a}和{b}的交集为:{a.intersection(b)}')
    print(f'{a}和{b}的并集为:{a.union(b)}')
    print(f'{a}和{b}的差集为:{a.difference(b)}')


def pprint():
    a = int(input('整数：'))
    print(f'{a}的二进制为: {bin(a)}')
    print(f'{a}的八进制为：{oct(a)}')
    print(f'{a}的十六进制为: {hex(a)}')


def newList():
    xList = eval(input('输入[列表]:'))
    print(f'新列表为：{[x for x in xList if x % 2 == 0]}')


def dictOut():
    a = eval(input('输入[列表a]:'))
    b = eval(input('输入[列表b]:'))
    minLen = min(len(a), len(b))
    dict1 = {}
    for i in range(minLen):
        dict1[a[i]] = b[i]
    print(f'最终的字典为：{dict1}')


def reList():
    xList = eval(input('输入[列表]:'))
    yList = sorted(xList, reverse=True)
    print(f'原列表为:{xList}\t新列表为:{yList}')


def mulList():
    xList = eval(input('输入[列表]:'))
    res = 1
    for x in xList:
        res *= x
    print(f'所有整数连乘的结果为：{res}')


def Mhd():
    lstA = eval(input('输入[列表a] (两个元素,下同):'))
    lstB = eval(input('输入[列表b]:'))
    print(f'曼哈顿距离为{abs(lstA[0] - lstB[0]) + abs(lstA[1] - lstB[1])}')


def dictList():
    lst = eval(input('包含若干集合的列表 [{},{},.....]:'))
    print(f'列表中集合的并集为{reduce(lambda x, y: x | y, lst)}')


def nSum():
    s0, q, n = input('输入等比数列首项、公比、项数:').split()
    sumN = 0
    for i in range(int(n)):
        sumN += int(s0) * int(q) ** int(i)
    print(f'前n项和为:{sumN}')


def strNum():
    sStr = eval(input("输入一个字符串 'xxxxxxx':"))
    setA = {}
    for x in sStr:
        if x not in setA.keys():
            setA[x] = 0
        setA[x] += 1
    print(f'统计结果:{setA}')


def Mtkl():
    n = int(input('输入次数:'))
    hits = 0
    for i in range(n):
        x = ran.random() * 2 - 1  # x∈(-1,1)
        y = ran.random() * 2 - 1  # y∈(-1,1)
        if x ** 2 + y ** 2 <= 1:  # 在圆内或圆周上
            hits += 1
    pi = (hits * 4) / n
    print(f'计算π的近似值为 {pi}')


if __name__ == '__main__':
    # numAdd()  # 各位数字之和
    # setAdd()  # 集合交、并、差集
    # pprint()  # 二、八、十六进制
    # newList()  # 偶数列表
    # dictOut()  # A、B列表生成字典
    # reList()  # 倒序输出
    # mulList()  # 列表各元素相乘
    # Mhd()  # 曼哈顿距离
    # dictList()  # 输出列表中集合的并集
    # nSum()  # 等比数列前n项和
    # strNum()  # 字符串中各字符的数目
    Mtkl()  # 蒙特卡洛方法计算π
