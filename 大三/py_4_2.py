class MyArray:
    def ___isNumber(self, n):
        if not isinstance(n, (int, float, complex)):
            return False
        return True

    # 构造函数，进行必要的初始化
    def __init__(self, *args):
        if not args:
            self.__value = []
        else:
            for arg in args:
                if not self.___isNumber(arg):
                    print('All elements must be numbers')
                    return
            self.__value = list(args)

    def getValue(self):
        return self.__value

    # 析构函数，释放内部封装的列表
    def __del__(self):
        del self.__value

    # 重载运算符+
    def __add__(self, other):
        """数组中每个元素都与数字other相加，或者两个数组相加，得到一个新数组"""
        if self.___isNumber(other):
            # 数组与数字other相加
            b = MyArray()
            b.__value = [item + other for item in self.__value]
            return b
        elif isinstance(other, MyArray):
            # 两个数组对应元素相加
            if len(other.__value) == len(self.__value):
                c = MyArray()
                c.__value = [i + j for i, j in zip(self.__value, other.__value)]
                return c
            else:
                print('Length no equal')
        else:
            print('Not supported')

    # 重载运算符-
    def __sub__(self, other):
        """数组元素与数字other做减法，得到一个新数组"""
        if self.___isNumber(other):
            # 数组与数字other相加
            b = MyArray()
            b.__value = [item - other for item in self.__value]
            return b
        elif isinstance(other, MyArray):
            # 两个数组对应元素相加
            if len(other.__value) == len(self.__value):
                c = MyArray()
                c.__value = [i - j for i, j in zip(self.__value, other.__value)]
                return c
            else:
                print('Length no equal')
        else:
            print('Not supported')

    # 重载运算符*
    def __mul__(self, other):
        """数组元素与数字other做乘法，或者两个数组相乘，得到一个新数组"""
        if self.___isNumber(other):
            # 数组与数字other相加
            b = MyArray()
            b.__value = [item * other for item in self.__value]
            return b
        elif isinstance(other, MyArray):
            # 两个数组对应元素相加
            if len(other.__value) == len(self.__value):
                c = MyArray()
                c.__value = [i * j for i, j in zip(self.__value, other.__value)]
                return c
            else:
                print('Length no equal')
        else:
            print('Not supported')

    def __truediv__(self, other):
        """数组元素与数字other做乘法，或者两个数组相乘，得到一个新数组"""
        if self.___isNumber(other):
            # 数组与数字other相加
            b = MyArray()
            b.__value = [item / other for item in self.__value]
            return b
        elif isinstance(other, MyArray):
            # 两个数组对应元素相加
            if len(other.__value) == len(self.__value):
                c = MyArray()
                c.__value = [i / j for i, j in zip(self.__value, other.__value)]
                return c
            else:
                print('Length no equal')
        else:
            print('Not supported')

    def __getitem__(self, index):
        length = len(self.__value)
        if isinstance(index, int) and 0 <= index < length:
            return self.__value[index]
        elif isinstance(index, (list, tuple)):
            for i in index:
                if not (isinstance(i, int)) and 0 <= i < length:
                    return 'index error'
                result = []
                for item in index:
                    result.append(self.__value[item])
                return result
            else:
                return 'index error'

    def __contains__(self, v):
        return v in self.__value

    def dot(self, v):
        if not isinstance(v, MyArray):
            raise Exception(v, 'must be an instance of MyArray')
        if len(v) != len(self.__value):
            raise Exception('The size must be equal')
        return sum([i * j for i, j in zip(self.__value, v.__value)])

    def __eq__(self, v):
        assert isinstance(v, MyArray), 'wrong type'
        return self.__value == v.__value

    def __lt__(self, v):
        assert isinstance(v, MyArray), 'wrong type'
        return self.__value < v.__value

    # 重载数组len，支持对象直接使用len()方法
    def __len__(self):
        return len(self.__value)

    # 支持使用print()函数查看对象的值
    def __str__(self):
        return str(self.__value)


if __name__ == "__main__":
    print('Please use me as a module.')
    x = MyArray(1, 12, 15, 14, 1)
    y = MyArray(2, 23, 16, 15, 2)
    print('%s\n array length:%d' % (x, len(x)))
    x = x + 2
    print(x.getValue)
    x = x - 2
    print(x.getValue)
    x = x * 2
    print(x.getValue)
    print(2 in y)  # 成员检测
    print(x.dot(y))  # 内积
    print(x < y)  # 大小比较
    print(x[2])  # 元素访问
