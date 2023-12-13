# 1040
# 1109
from collections import deque
import copy

def find_group(r, l, cards, pre_visited):
    visited = copy.deepcopy(pre_visited)
    que = deque([r])
    visited[r] = True
    count = 1
    while que:
        index = que.popleft()
        value = cards[index]

        if value <= l and visited[value] == False:
            que.append(value)
            visited[value] = True
            count +=1
    return count
            
def solution(cards):
    answer = 0
    l = len(cards)
    cards = [0] + cards
    
    #임의의 상자 선택하는 로직
    for r in range(1, l + 1): 
        # r = 1 # 첫번째 선택 가정
        visited = [False for _ in range(l + 1)]
        visited[0] = True

        que = deque([r])
        visited[r] = True
        count1 = 1
        # 상자 선택해 그룹 1
        while que:
            index = que.popleft()
            value = cards[index]
            if value <= l and visited[value] == False:
                que.append(value)
                visited[value] = True
                count1 +=1

        # 상자 선택해 그룹 2  
        count2 = 0
        if False in visited:
            for n, v in enumerate(visited):
                if v == False:
                    count2 = max(count2, find_group(n, l, cards, visited ))
        answer = max(answer, count1 * count2)
    return answer