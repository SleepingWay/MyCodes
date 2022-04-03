n, m = map(int, input().split())
strr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(n):
    tmp = strr[i:max(i - m, 0):-1] + strr[0:max(m - i, 0):1]
    print(tmp)
