
def proc(n):
    lst1 = list(str(n))
    lst2 = lst1[::-1]
    lst1 = lst1 + lst2
    str1 = ''.join(lst1)
    return int(str1)


for i in range(10, 100):
    res = proc(i)
    print(res)
