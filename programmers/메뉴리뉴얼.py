from itertools import combinations

def solution(orders, course):
    answer = []
    l = course[-1] + 1
    total_answer = {}
    total_set = [set() for _ in range(l)]
    orders.sort(key=lambda x:-len(x))
    
    for order in orders:
        for num in course:
            for s in combinations(order, num):
                k = "".join(sorted(s))
                total_set[num].add(k)
                if k in total_answer:
                    total_answer[k] += 1
                else:
                    total_answer[k]  = 1

    for i in range(l - 1, -1, -1):
        max_arr = [set() for _ in range(l)]
        for k in total_set[i]:
            kk = total_answer[k]
            if kk >= 2 and l - 1 >= kk :
                max_arr[kk].add(k)

        for ii in range(l-1, -1, -1):
            if len(max_arr[ii]) == 0:
                continue
            else :
                answer += max_arr[ii]
                break
    
    return sorted(answer)