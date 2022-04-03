import copy


def Input():
    start = int(input('请输入开始时的磁道号:'))
    newList = list(map(int, input('请输入访问的磁道序列:').split()))
    return start, newList


def DiskFCFS(lst, begin):   # 先来先服务
    distanceSum = 0
    now = begin
    for x in lst:
        distanceSum += abs(now - x)
        now = x
    print('FCFS的访问序列为: {}\nFCFS的平均寻道距离为: {}'.format(lst, distanceSum / len(lst)))


def DiskSSTF(lst, begin):   # 最短寻道时间优先
    distanceSum = 0
    lst_1 = copy.copy(lst)
    newList = []    # 访问序列
    now = begin
    for j in range(len(lst)):
        disMap = {}
        for x in lst_1:
            disMap[x] = abs(x - now)
        disMap = dict(sorted(disMap.items(), key=lambda i: i[1]))   # 每进行一次访问排一次序，找到距离当前磁道最近的
        keys = list(disMap.keys())
        values = list(disMap.values())
        newList.append(keys[0])
        distanceSum += values[0]    # 每次加最短距离
        now = keys[0]
        lst_1.remove(keys[0])
    print('SSTF的访问序列为: {}\nSSTF的平均寻道距离为: {}'.format(newList, distanceSum / len(lst)))


def DiskSCAN(lst, begin):   # 电梯调度
    distanceSum = 0
    now = begin
    newList = []    # 访问序列
    list1 = [x for x in lst if x > now]     # 将在当前磁道 前和后 的磁道分开存放并排序
    list2 = [x for x in lst if x < now]
    list1.sort()
    list2.sort(reverse=True)
    for x in list1:
        distanceSum += abs(x - now)
        now = x
        newList.append(now)
    for x in list2:
        distanceSum += abs(x - now)
        now = x
        newList.append(now)
    print('SCAN的访问序列为: {}\nSCAN的平均寻道距离为: {}'.format(newList, distanceSum / len(lst)))

if __name__ == '__main__':
    disk = [55, 58, 39, 18, 90, 160, 150, 38, 184]
    Start = 100
    # Start, disk = Input()
    DiskFCFS(disk, Start)
    DiskSSTF(disk, Start)
    DiskSCAN(disk, Start)
