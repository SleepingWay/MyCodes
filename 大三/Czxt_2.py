name = 0  # 程序名
arriveTime = 1  # 到达时间
serverTime = 2  # 服务时间
startTime = 3  # 开始时间
finishTime = 4  # 完成时间
wholeTime = 5  # 周转时间
valueWholeTime = 6  # 带权周转时间
priority = 7  # 优先权


def pcbInput(pcb, i):  # 输入程序数据
    for x in range(int(i)):
        plist = input('依次输入程序名 到达时间 服务时间：').split()
        pcb.append(plist)


def pcbInit(pcb, i):  # 对程序数据初始化
    for j in range(int(i)):
        pcb[j][arriveTime] = int(pcb[j][arriveTime])
        pcb[j][serverTime] = int(pcb[j][serverTime])
        pcb[j][len(pcb[j]):] = [0] * (priority - serverTime)


def pprint(pcb, i):
    averWholeTime, averValueWholeTime = 0, 0
    print('程序名\t到达时间\t服务时间\t开始时间\t完成时间\t周转时间\t带权周转时间\t优先权\n')
    for j in range(int(i)):
        for x in pcb[j]:
            print(x, end='\t\t')
        print('\n')
    for j in range(int(i)):
        averWholeTime += pcb[j][wholeTime]
        averValueWholeTime += pcb[j][valueWholeTime]
    averWholeTime = float(averWholeTime) / float(i)
    averValueWholeTime = float(averValueWholeTime) / float(i)
    print("该组的平均周转时间为：{}\t\t平均带权周转时间为：{}".format(averWholeTime, averValueWholeTime))


def prio(pcb, i):  # 优先权调度算法
    pcb.sort(key=lambda x: x[priority])
    time = pcb[0][arriveTime]
    for j in range(int(i)):
        if j == 0:
            pcb[j][startTime] = pcb[j][arriveTime]
        else:
            if pcb[j][arriveTime] > time:
                pcb[j][startTime] = pcb[j][arriveTime]
            else:
                pcb[j][startTime] = pcb[j - 1][finishTime]
        pcb[j][finishTime] = pcb[j][startTime] + pcb[j][serverTime]
        pcb[j][wholeTime] = pcb[j][finishTime] - pcb[j][arriveTime]
        pcb[j][valueWholeTime] = float(pcb[j][wholeTime]) / float(pcb[j][serverTime])
        time = pcb[j][finishTime]


def RR(pcb, i, q):  # 时间片轮转调度算法
    flag = [0] * int(i)
    finish = [1] * int(i)
    time = 0
    while 1:
        for j in range(int(i)):
            if j == 0:
                pcb[j][startTime] = pcb[j][arriveTime]
            else:
                if pcb[j][arriveTime] > time:
                    pcb[j][startTime] = pcb[j][arriveTime]
                elif pcb[j][arriveTime] < time and pcb[j][startTime] == 0:
                    pcb[j][startTime] = pcb[j - 1][finishTime]
                else:
                    if pcb[j][startTime] == 0 and pcb[j][arriveTime] != 0:
                        pcb[j][startTime] = time

            if flag[j] == 0:  # 该程序没有完成
                pcb[j][finishTime] += int(q)
                time += int(q)
                if pcb[j][finishTime] == pcb[j][serverTime]:
                    flag[j] = 1
                    pcb[j][finishTime] = time
                elif pcb[j][finishTime] > pcb[j][serverTime]:
                    flag[j] = 1
                    pcb[j][finishTime] = pcb[j][startTime] + pcb[j][serverTime]
                    time = pcb[j][finishTime]
        same = 0
        for j in range(int(i)):
            if flag[j] != finish[j]:
                same += 1
        if same == 0:
            for j in range(int(i)):
                pcb[j][wholeTime] = pcb[j][finishTime] - pcb[j][arriveTime]
                pcb[j][valueWholeTime] = float(pcb[j][wholeTime]) / float(pcb[j][serverTime])
            break


n = input("输入进程数目：")
PCB = list()
pcbInput(PCB, n)
pcbInit(PCB, n)
x = input("输入1运行非抢占优先权调度，输入2运行时间片轮转调度：")
if x == '1':
    for i in range(int(n)):
        PCB[i][priority] = input("请输入第{}个程序的优先权:".format(i + 1))
    prio(PCB, n)
elif x == '2':
    q = input("输入时间片大小:")
    RR(PCB, n, q)
pprint(PCB, n)
