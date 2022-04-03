s = "***|**|*****|**||**|*"
queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]


def platesBetweenCandles(s, queries):
    answer = [0] * len(queries)
    sum = [0] * len(s)
    tmp = {}
    for i in range(len(s)):
        if s[i] == '*':
            sum[i] = 1
    for i in range(1, len(s)):
        sum[i] += sum[i - 1]
    for i in range(len(queries)):
        for j in range(queries[i][0], queries[i][1] + 1):
            if s[j] == '|':
                tmp[i] = [j, 0]
                break
            else:
                tmp[i] = [0, 0]
        for j in range(queries[i][1] - queries[i][0] + 1):
            if s[queries[i][1] - j] == '|':
                tmp[i][1] = queries[i][1] - j
                break
    for i in range(len(queries)):
        answer[i] = sum[tmp[i][1]] - sum[tmp[i][0]]
    return answer


print(platesBetweenCandles(s, queries))
