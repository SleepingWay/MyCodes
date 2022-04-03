def FIFO(queue, blockNum):
    livTime = {}  # 各页在块中存在的时间
    for x in queue:
        livTime[x] = 0
    block = []  # 块中存在的页
    hit = 'HIT!'
    print('先进先出置换算法(FIFO) :')
    for x in queue:
        if len(block) < blockNum and x not in block:  # 块内未满且下一页不在块内 继续添加
            block.append(x)
            livTime[x] = 0
            for y in block:  # 除了刚进入块的页存在时间加1
                if y in livTime.keys() and y != x:
                    livTime[y] += 1
            hit = 'LOST!'
        elif len(block) < blockNum and x in block:  # 块内未满且下一页在块内
            for y in block:
                if y in livTime.keys():
                    livTime[y] += 1
            hit = 'HIT!'
        elif x not in block:  # 块已满 找出存在时间最长的替换
            num = block[0]
            maxTime = livTime[num]
            index = block.index(num)
            for y in block:
                if livTime[y] > maxTime:
                    maxTime = livTime[y]
                    num = y
                    index = block.index(y)
            livTime[num] = 0
            block[index] = x
            for y in block:
                if y in livTime.keys() and y != x:
                    livTime[y] += 1
            hit = 'LOST!'
        else:
            for y in block:
                if y in livTime.keys():
                    livTime[y] += 1
            hit = 'HIT!'
        print(x, '\t', block, '\t', hit)


def OPT(queue, blockNum):
    hit = 'LOST!'
    block = []  # 页内存在的块
    print('最佳置换算法(OPT) :')
    for i, x in enumerate(queue):
        if len(block) < blockNum and x not in block:
            block.append(x)
            hit = 'LOST!'
        elif len(block) < blockNum and x in block:
            hit = 'HIT!'
        elif x in block:
            hit = 'HIT!'
        elif x not in block:  # 块满且下一页不在块内
            index = i
            maxLength = 0
            nowLength = 0
            num = 0
            for y in block:  # 选出最长（未来）时间内不再被访问的页面
                nowLength = 0
                for j in range(index + 1, len(queue), 1):
                    if queue[j] != y:
                        nowLength += 1
                    else:
                        break
                if nowLength > maxLength:
                    maxLength = nowLength
                    num = block.index(y)
            block[num] = x
            hit = 'LOST!'
        print(x, '\t', block, '\t', hit)


def LRU(queue, blockNum):  # 相比于FIFO只多了一个当页在块内时，将该页的存在时间置零的操作
    livTime = {}  # 各页在块中存在的时间
    for x in queue:
        livTime[x] = 0
    block = []  # 块中存在的页
    hit = 'HIT!'
    print('最近最久未使用算法（LRU） :')
    for x in queue:
        if len(block) < blockNum and x not in block:  # 块内未满且下一页不在块内 继续添加
            block.append(x)
            livTime[x] = 0
            for y in block:  # 除了刚进入块的页存在时间加1
                if y in livTime.keys() and y != x:
                    livTime[y] += 1
            hit = 'LOST!'
        elif len(block) < blockNum and x in block:  # 块内未满且下一页在块内
            for y in block:
                if y in livTime.keys():
                    livTime[y] += 1
            hit = 'HIT!'
        elif x not in block:  # 块已满 找出存在时间最长的替换
            num = block[0]
            maxTime = livTime[num]
            index = block.index(num)
            for y in block:
                if livTime[y] > maxTime:
                    maxTime = livTime[y]
                    num = y
                    index = block.index(y)
            livTime[num] = 0
            block[index] = x
            for y in block:
                if y in livTime.keys() and y != x:
                    livTime[y] += 1
            hit = 'LOST!'
        else:
            for y in block:
                if y in livTime.keys() and y != x:
                    livTime[y] += 1
                elif y == x:
                    livTime[x] = 0  # 存在时间置零
            hit = 'HIT!'
        print(x, '\t', block, '\t', hit)


if __name__ == '__main__':
    Queue = eval(input('请输入调用页的队列 <输入样例 [1,2,0,2]> :'))
    bNum = int(input('请输入分配给该作业的主存块数 :'))
    # FIFO(Queue, bNum)
    # OPT(Queue, bNum)
    LRU(Queue, bNum)
