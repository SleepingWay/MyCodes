import copy
Num = 0  # 进程序号
Max = 1  # 最大需求矩阵
Allocation = 2  # 分配矩阵
Need = 3  # 需求矩阵


def pInput(pro, proNum, res, resourceNum):
    for i in range(proNum):
        pro.append([])
        plist = int(input('请输入进程序号：'))
        pro[i].append(plist)
        plist = input('请输入最大需求矩阵：').split()
        plist = list(map(int, plist))
        pro[i].append(plist)
        plist = input('请输入分配矩阵：').split()
        plist = list(map(int, plist))
        pro[i].append(plist)
        plist = input('请输入需求矩阵：').split()
        plist = list(map(int, plist))
        pro[i].append(plist)
    for i in range(resourceNum):
        r = int(input('请输入第{}个资源总数目：'.format(i + 1)))
        res.append(r)


def pInit(pro, proNum, res, resNum):
    for i in range(proNum):
        for j in range(resNum):
            res[j] -= pro[i][Allocation][j]
    return res


def pPrint():
    print('进程序号\tWork\tNeed\tAllocation\tWork+Allocation\tFinish\n')
    return


def bankerAlgorithm(pro, proNum, available, resNum):
    pro1 = copy.copy(pro)
    available1 = copy.copy(available)
    finish = [0] * proNum
    doIt = 0
    num = 0
    sum = [0] * resNum
    while True:
        for k in range(proNum):  # 至多需要proNum遍才能确定系统是否安全
            for i in range(proNum):
                doIt = 0
                for j in range(resNum):
                    if pro1[i][Need][j] <= available1[j]:
                        doIt += 1
                    else:
                        doIt += 0
                if finish[i] == 0 and doIt == resNum:
                    num += 1
                    finish[i] = 1
                    for j in range(resNum):
                        sum[j] = available1[j] + pro1[i][Allocation][j]
                    print(
                        '{}\t{}\t{}\t{}\t{}\t{}\n'.format(pro1[i][Num], available1, pro1[i][Need], pro1[i][Allocation], sum, finish[i]))
                    for j in range(resNum):
                        available1[j] += pro1[i][Allocation][j]
            if num == 0:  # 如果一轮下来没有符合条件的程序，则说明系统不安全
                print('没有安全序列')
        return


def securityAlgorithm(pro, proNum, resNum, available, requestNum, request):
    tryAvailable = available
    doIt = 0
    for i in range(resNum):
        if pro[requestNum][Need][i] >= request[i]:
            doIt = 1
        else:
            doIt = 0
    # 循环结束时，如果doIt = 1 则说明没有超过该程序所需的最大资源数
    if doIt == 1:
        for i in range(resNum):
            if tryAvailable[i] >= request[i]:
                doIt = 1
            else:
                doIt = 0
    # 循环结束时，如果doIt = 1 则说明可以尝试将资源分配给该程序
    else:
        print('所需资源已超过该程序所需的最大值.\n')
        return 0
    if doIt == 1:  # 进行资源分配
        for i in range(resNum):
            tryAvailable[i] -= request[i]
            pro[requestNum][Allocation][i] += request[i]
            pro[requestNum][Need][i] -= request[i]
    finish = [0] * proNum
    work = tryAvailable
    doIt = 0
    num = 0
    sum = [0] * resNum
    while True:
        for k in range(proNum):  # 至多需要proNum遍才能确定系统是否安全
            for i in range(proNum):
                doIt = 0
                for j in range(resNum):
                    if pro[i][Need][j] <= work[j]:
                        doIt += 1
                    else:
                        doIt += 0
                if finish[i] == 0 and doIt == resNum:
                    num += 1
                    finish[i] = 1
                    for j in range(resNum):
                        sum[j] = work[j] + pro[i][Allocation][j]
                    print('{}\t{}\t{}\t{}\t{}\t{}\n'.format(pro[i][Num], work, pro[i][Need], pro[i][Allocation], sum,
                                                            finish[i]))
                    for j in range(resNum):
                        work[j] += pro[i][Allocation][j]
            if num == 0:  # 如果一轮下来没有符合条件的程序，则说明系统不安全
                return 0
        if 0 in finish:
            return 0
        else:
            return 1


pro = list()
res = list()
proNum = int(input('请输入进程数：'))
resNum = int(input('请输入资源数：'))
pInput(pro, proNum, res, resNum)
available = pInit(pro, proNum, res, resNum)
requestNum = int(input('请输入请求资源的进程号：'))
request = input('请输入所请求的资源：').split()
request = list(map(int, request))
pPrint()
bankerAlgorithm(pro, proNum, available, resNum)
pPrint()
Safety = securityAlgorithm(pro, proNum, resNum, available, requestNum, request)
if Safety == 1:
    print('系统处于安全状态，可以分配，具体分配如上表.\n')
    for i in range(resNum):
        available[i] -= request[i]
        pro[requestNum][Allocation][i] += request[i]
        pro[requestNum][Need][i] -= request[i]
else:
    print('系统处于不安全状态，不能进行分配.\n')
