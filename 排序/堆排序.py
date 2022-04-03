class HeapSort:
    def heapsort(self, lst):
        if len(lst) < 2:
            return
        for i in range(len(lst)):
            self.heapInsert(lst, i)
        heapSize = len(lst)
        while heapSize > 0:
            heapSize -= 1
            self.swap(lst, 0, heapSize)
            self.heapify(lst, 0, heapSize)

    def heapify(self, lst, i, heapSize):
        left = i * 2 + 1
        while left < heapSize:
            # 找出最大的孩子
            largest = left + 1 if left + 1 < heapSize and lst[left] < lst[left + 1] else left
            # 找出父亲与较大孩子中最大的
            largest = i if lst[i] > lst[largest] else largest
            if largest == i:
                break
            self.swap(lst, largest, i)
            i = largest
            left = i * 2 + 1

    def heapInsert(self, lst, i):
        while lst[i] > lst[int((i - 1) / 2)]:
            self.swap(lst, i, (i - 1) // 2)
            i = (i - 1) // 2

    def swap(self, lst, i, j):
        t = lst[i]
        lst[i] = lst[j]
        lst[j] = t

    def main(self):
        lst = [1, 3, 2, 2, 1, 3]
        self.heapsort(lst)
        print(lst)


test = HeapSort()
test.main()
