from collections import deque

def sum_len(arr):
    s = 0
    l = 0
    for i in arr:
        s += i
        l +=1
    return [s, l]

def solution(queue1, queue2):
    answer = 0
    sum1, l1  = sum_len(queue1)
    sum2, l2  = sum_len(queue2)
    sum_bias = (sum1 + sum2) /2
    
    limit = l1 + l2
    count = 0
    
    if (sum1 + sum2 )% 2 != 0:
        return -1
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    while sum1 != sum2:
        if answer > limit:
            return -1
        
        # 총합이 큰놈을 뺀다
        while q1 and sum1 > sum2:
            v = q1.popleft()
            q2.append(v)
            sum1 -= v
            sum2 += v
            answer +=1
            
        while q2 and sum1 < sum2:
            v = q2.popleft()
            q1.append(v)
            sum2 -= v
            sum1 += v
            answer +=1
    
    


    
    
    
    return answer