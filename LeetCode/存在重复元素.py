def hhh():
    nums = [1, 2, 3, 1]
    tmp = {}
    for i, x in enumerate(nums):
        tmp[i] = x
    for i in tmp.keys():
        for j in tmp.keys():
            if tmp[i] == tmp[j] and i != j:
                return True
    return False


if hhh():
    print("True")
else:
    print("False")
