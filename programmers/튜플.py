import re
import heapq

def solution(s):
    answer = []
    p = re.compile('{[0-9,]+}')
    arr = p.findall(s[1:-1])
    heap = []
    
    for x in arr:
        local_tuple = x[1:-1].split(',')
        heapq.heappush(heap, (len(local_tuple), local_tuple))
    
    answer_candidate = []
    while heap:
        a = heapq.heappop(heap)[1]
        for x in a:
            if x not in answer_candidate:
                answer_candidate.append(x)
                break
        
    return [int(x) for x in answer_candidate]