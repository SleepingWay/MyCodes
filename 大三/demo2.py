import math

def gcd(a, b):
    m, n = a, b
    while b != 0:
        c = math.floor(a / b)
        r = a - c * b
        a = b
        b = r
    return a
    # print('The gcd of {} and {} is {}'.format(m, n, a))
#
def ext_gcd(a, b):
    if b == 0:
        return 1, 0
    else:
        x, y = ext_gcd(b, a % b)
        x, y = y, (x - (a // b) * y)
        return x, y

# a, b = map(int, input("Please input :").split())
# gcd(a, b)
a,b = map(int,input("Please input () mod () :").split())
m,n = ext_gcd(a,b)
print("The multiplication inverse element of {} is {}".format(a,m))

# num = 0
# for i in range(2022):
#     if i != 0:
#         if gcd(i,2021)>1:
#             num += 1
#             print(num)
