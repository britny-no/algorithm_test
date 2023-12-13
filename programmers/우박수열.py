
def solution(k, ranges):
    answer = []
    
    # 우박수열 graph 생성
    graph = []
    n = 1
    while k != 1:
        graph.append(k)
        n += 1
        if k % 2 == 0:
            k = k // 2
        else:
            k = k*3 + 1
    graph.append(1)

    for a, b in ranges:
        s = 0
        if a > n + b - 1:
            s = -1
        else:
            for i in range(a, n + b - 1):
                big = max(graph[i+1], graph[i])
                small = min(graph[i+1], graph[i])
                s += big - (0.5 *(big - small) )
        answer.append(s)
    return answer