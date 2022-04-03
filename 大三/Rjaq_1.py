def hahaha(lpstr, name):
    xlist = []
    for j in range(len(name)):
        xlist.append(ord(name[j]))
    byte = [7, 13, 17, 19, 31, 63, 53, 71]
    ebx = 1
    strsum = 0
    for x in range(len(name)):
        ebx *= 10
        strsum += xlist[x] * byte[x % 8]
    strr = strsum % ebx
    print("Right!") if strr == lpstr else print("False!")
    print("The correct lpstr is '{}'.".format(strr))

name, lpstr = input("依次输入用户名，序列号：").split()

hahaha(lpstr, name)
