for i in range(100, 1000):
    num = i
    a = num % 10
    num = num // 10
    b = num % 10
    c = num // 10
    if (a * a * a + b * b * b + c * c * c) == i:
        print(i)
