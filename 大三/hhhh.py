# s = 'FFEEFEAAECFFBDBFBCDADACDEEDCCFFAFADEFBBAFDCDDCDBFEFCEDDBFDBEEFCAAEECEECDCDECADDCDFAEACECFEADC' \
#     'BFECADFDFBAAADCFAFFCEADFDDAEAFAFFDEFECEDEEEDFBDBFDDFFBCFACECEDCAFAFEFAFCDBDCCBCCEADADAEBAFBACA' \
#     'CBFCBABFDAFBEFCFDCFBCEDCEAFBCDBDDBDEFCAAAACCFFCBBAAEECFEFCFDEEDCACDACECFFBAAAFACDBFFAEFFCCCDBFA' \
#     'DDDBEBCBEEDDECFAFFCDEAFBCBBCBAEDFDBEBBBBABBFDECBCEFAABCBCFFBDBACCFFABEAEBEACBBDCBCCFADDCACFDEDECCC' \
#     'BFAFCBFECAACAFBCFBAF'
# dictt = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0}
# for x in s:
#     dictt[x] += 1
# print(dictt)

# import math
#
#
# class Solution:
#     def __init__(self):
#         self.num = 0
#         self.money = 0
#
#     def result(self, p, t):
#         self.num = math.ceil(t / 12)
#         self.money = p * self.num
#
#     def print(self):
#         print(self.money)
#
# p, t = input().split()
# res = Solution()
# res.result(int(p), int(t))
# res.print()

# class Solution:
#     def __init__(self):
#         self.flag = 0
#
#     def Judge(self, a, b, c):
#         xlist = [a, b, c]
#         xlist.sort()
#         if xlist[0]**2 + xlist[1]**2 == xlist[2]**2:
#             self.flag = 1
#
#     def Pprint(self):
#         if self.flag == 1:
#             print('YES')
#         else:
#             print('NO')
#
# a,b,c = input().split()
# a,b,c = int(a),int(b),int(c)
# res = Solution()
# res.Judge(a,b,c)
# res.Pprint()


# n = input()
# b = input()
# a = []
# hashmap = {}
# xList = []
# flag = {}
# for i in b.split():
#     a.append(int(i))
# for i, num in enumerate(a):
#     hashmap[num] = i+1
#     flag[num] = 0
# people = 0
# for x in hashmap.keys():s
#     while flag[x] != 1:
#         if x not in xList:
#             flag[x] = 1
#             xList.append(x)
#             x = hashmap[x]
#             if flag[x] == 1:
#                 xList = []
#                 people += 1
# print(people)

n = int(input())
