from collections import deque

def solution(numbers, target):
    answer = 0
    end = len(numbers)
    
    que  = deque([(0, 0)])
    
    while que:
        index, value = que.popleft()
        
        if end == index:
            if target == value:
                answer +=1
        else:
            que.append((index+1, value +  -1 * numbers[index]))
            que.append((index+1, value + numbers[index]))
    
    
    return answer