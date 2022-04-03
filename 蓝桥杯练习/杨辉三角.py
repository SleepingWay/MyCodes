n = int(input())
lst = []
old = []
for i in range(n):
    lst = []
    if i == 0:
        lst.append(1)
    else:
        for j in range(i + 1):
            if 0 < j < i:
                lst.append(old[j] + old[j - 1])
            else:
                lst.append(1)
    print(' '.join(str(x) for x in lst))
    old = lst[:]
