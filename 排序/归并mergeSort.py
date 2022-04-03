def process(lst, L, R):
    if L == R:
        return
    mid = L + ((R - L) >> 1)
    process(lst, L, mid)
    process(lst, mid + 1, R)
    merge(lst, L, mid, R)
    print(lst)


def merge(lst, L, mid, R):
    tmp = []
    p1 = L
    p2 = mid + 1
    while p1 <= mid and p2 <= R:
        if lst[p1] <= lst[p2]:
            tmp.append(lst[p1])
            p1 += 1
        else:
            tmp.append(lst[p2])
            p2 += 1
    while p1 <= mid:
        tmp.append(lst[p1])
        p1 += 1
    while p2 <= R:
        tmp.append(lst[p2])
        p2 += 1
    for i in range(len(tmp)):
        lst[L + i] = tmp[i]


def main():
    lst = [3, 2, 1, 5, 6, 2]
    process(lst, 0, len(lst) - 1)
    print(lst)


if __name__ == '__main__':
    main()
