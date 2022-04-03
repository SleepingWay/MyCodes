import time


class MyQueue:
    def __init__(self, size):
        self._content = []
        self._size = size
        self.__cur = 0
        print('食堂窗口最多支持 {} 人同时打饭，多的人要排队'.format(size))

    def setSize(self, size):
        if size < self.__cur:
            # 如果缩小队列，应删除后面的元素
            for i in range(size, self.__cur)[::-1]:
                del self._content[i]
            self.__cur = size
        self._size = size

    def put(self, v, timeout=10):
        # 模拟入队，在列表尾部追加元素
        if self.__cur < self._size:
            self._content.append(v)
            self.__cur = self.__cur + 1
        else:
            # 队列满，阻塞，超时放弃
            for i in range(timeout):
                time.sleep(1)
                print('等待1秒后可排队')
                break
            else:
                print('超时')

    def get(self, timeout=10):
        # 模拟出队，从列表头部弹出元素
        if self._content:
            self.__cur = self.__cur - 1
            return self._content.pop(0)
        else:
            # 队列为空，阻塞，超时放弃
            for i in range(timeout):
                time.sleep(1)
                print('等待1秒后饭已打好')
                if self._content:
                    self.__cur = self.__cur - 1
                    return self._content.pop(0)
                    # pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值

    def show(self):
        # 如果列表非空，输出列表
        if self._content:
            print(self._content)
        else:
            print('The queue is empty')

    def qsize(self):
        return self.__cur

    def empty(self):
        self._content = []
        self.__cur = 0

    def isEmpty(self):
        return not self._content

    def isFull(self):
        return self.__cur == self._size

if __name__ == '__main__':
    q = MyQueue(2)  # 食堂窗口最多支持2人同时打饭
    print("---第一人进入")
    q.put("A")
    print("---队列大小{0}---是否满{1}---是否空{2}---".format(q.qsize(), q.isFull(), q.isEmpty()))

    print("---第二人进入")
    q.put("B")
    print("---队列大小{0}---是否满{1}---是否空{2}---".format(q.qsize(), q.isFull(), q.isEmpty()))

    print("---第三人尝试进入进入")
    q.put("C")
    print("---队列大小{0}---是否满{1}---是否空{2}---".format(q.qsize(), q.isFull(), q.isEmpty()))

    # 一名小伙将排队扩容
    q.setSize(3)

    print("---第三人进入")
    q.put("C")
    print("---队列大小{0}---是否满{1}---是否空{2}---".format(q.qsize(), q.isFull(), q.isEmpty()))

    print("---第一人走出")
    print(q.get())
    print("---队列大小{0}---是否满{1}---是否空{2}---".format(q.qsize(), q.isFull(), q.isEmpty()))

    print("---第二人走出")
    print(q.get())
    print("---队列大小{0}---是否满{1}---是否空{2}---".format(q.qsize(), q.isFull(), q.isEmpty()))

    print("---第三人走出")
    print(q.get())
    print("---队列大小{0}---是否满{1}---是否空{2}---".format(q.qsize(), q.isFull(), q.isEmpty()))
