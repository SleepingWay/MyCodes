def proc1(n, m):
    lst1 = list(str(n))
    lst2 = list(str(m))
    lst2 = lst2 + lst1
    str1 = ''.join(lst2) + ''.join(lst2[::-1])
    return int(str1)


def proc2(n, m):
    lst1 = list(str(n))
    lst2 = list(str(m))
    str1 = ''.join(lst2) + ''.join(lst1) + ''.join(lst2[::-1])
    return int(str1)


num = int(input())
lst = []
for i in range(0, 10):
    for j in range(10, 100):
        a = j // 10
        b = j % 10
        if (a + b + i) * 2 == num:      # 六位数
            res = proc1(i, j)
            lst.append(res)
        if (a + b) * 2 + i == num:      # 五位数
            res = proc2(i, j)
            lst.append(res)
lst.sort()      # 保证从小到大输出
for x in lst:
    print(x)
