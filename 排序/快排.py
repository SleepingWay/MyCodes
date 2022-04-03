import random as ran


class QuickSort:
    def qs(self, lst):
        if len(lst) < 2:
            return
        self.process(lst, 0, len(lst) - 1)

    def process(self, lst, l, r):
        if l < r:
            self.swap(lst, ran.randint(l, r), r)
            p = self.partition(lst, l, r)
            self.process(lst, l, p[0] - 1)
            self.process(lst, p[1] + 1, r)

    def swap(self, lst, i, j):
        t = lst[i]
        lst[i] = lst[j]
        lst[j] = t

    def partition(self, lst, l, r) -> list:
        small = l - 1   # 左边界
        large = r       # 右边界
        while l < large:    # l为当前指针
            if lst[l] > lst[r]:
                self.swap(lst, l, large - 1)
                large -= 1
            elif lst[l] < lst[r]:
                self.swap(lst, small + 1, l)
                small += 1
                l += 1
            else:
                l += 1
        self.swap(lst, large, r)
        return [small + 1, large]

    def Input(self):
        return list(map(int, input().split()))

    def pprint(self, lst):
        print(lst)

    def main(self):
        lst = self.Input()
        self.qs(lst)
        self.pprint(lst)


if __name__ == '__main__':
    a = QuickSort()
    a.main()

