# import math
# d, h = map(int, input().split())
# V = (3 * (d / 2) ** 2) * (h - 2)
# print(math.ceil(V / 8))

# Class = {'B': [2, 4], 'I': [2, 3], 'H': [5, 6]}
# num, classType = input().split()
# num = int(num)
# lst = []
# stu, gMax = 0, 0
# for i in range(num):
#     newLst = list(map(int, input().split()))
#     lst.append(newLst)
# for x in lst:
#     nowRes = x[Class[classType][0]] + x[Class[classType][1]]
#     if nowRes > gMax:
#         gMax = nowRes
#         stu = x[0]
# print(stu)

# num = int(input())
# lst = []
# for i in range(num):
#     newList = list(map(int, input().split()))
#     lst.append(newList)
# start = 0
# minlength, length = 99999999, 0
# flag = [0] * num
# for i in range(num):
#     maxnum = 0
#     length = 0
#     for x in lst:
#         if x[2] > maxnum and flag[lst.index(x)] == 0:
#             start = lst.index(x)
#             maxnum = x[2]
#     for x in lst:
#         if x != lst[start]:
#             length = length + (abs(x[0] - lst[start][0]) + abs(x[1] - lst[start][1])) * x[2]
#     if length < minlength:
#         minlength = length
#     flag[start] = 1
# print(minlength)

n, m, k = map(int, input().split())
lst = []
for i in range(n):
    newList = input()
    newList = [int(x) for x in newList]
    lst.append(newList)
start, minnum = 0, 99999999
nownum = 0
for i in range(n - m):
    nownum = 0
    for j in range(m):
        nownum += lst[i + j].count(1)
    if nownum < minnum:
        minnum = nownum
        start = i
print(minnum)