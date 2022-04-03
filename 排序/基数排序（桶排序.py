class RadixSort:
    def radixSort1(self, lst):
        if len(lst) < 2:
            return
        self.radixSort2(lst, 0, len(lst) - 1, self.bitNum(lst))

    def bitNum(self, lst):
        res = 0
        num = max(lst)
        while num != 0:
            res += 1
            num //= 10
        return res

    def bitGet(self, num, i):
        if i != 1:
            return int((num // (10 ** (i - 1))) % 10)
        else:
            return int(num % 10)

    def radixSort2(self, lst, i, j, digit):
        count = [0] * 10
        bucket = [0] * len(lst)
        for bit in range(digit):
            for num in range(i, j + 1):
                count[self.bitGet(lst[num], bit + 1)] += 1
            for num in range(1, 10):
                count[num] += count[num - 1]
            for num in range(j, i-1, -1):
                x = self.bitGet(lst[num], bit + 1)
                bucket[count[x] - 1] = lst[num]
                count[x] -= 1
            for num1, num2 in zip(range(i, j + 1), range(len(lst))):
                lst[num1] = bucket[num2]

    def main(self):
        lst = [3, 2, 1, 2, 7, 5]
        self.radixSort1(lst)
        print(lst)


test = RadixSort()
test.main()
