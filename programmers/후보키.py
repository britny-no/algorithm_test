# 0940
# 1058

from itertools import combinations
import heapq

def solution(relation):
    answer = 0
    column = len(relation[0])
    non_unique_arr = [x for x in range(column)]
    heap = []

    for count in range(1, len(non_unique_arr)+1):
        for index_arr in list(combinations(non_unique_arr, count)):
            case = []
            stop = False
            for arr in relation:
                text  = ""
                for i in index_arr:
                    text += arr[i]

                if text in case:
                    stop = True
                    break
                else:
                    case.append(text)

            if stop == False:
                heapq.heappush(heap, [len(index_arr), sorted(index_arr)])


    sub = []
    while heap:
        v = heapq.heappop(heap)[1]
        inter = False
        for vv in sub:
            if len(set(vv).intersection(v)) == len(vv):
                inter = True
                break

        if inter == False:
            answer +=1
            sub.append(v)
        
    
    
    return answer