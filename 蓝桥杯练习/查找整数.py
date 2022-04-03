n = int(input())
lst = list(map(int, input().split()))
num = int(input())
if num in lst:
    print(lst.index(num) + 1)
else:
    print(-1)
