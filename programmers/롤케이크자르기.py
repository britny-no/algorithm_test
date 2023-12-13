from collections import Counter

def solution(topping):
    answer = 0
    index = 1
    last_index = len(topping)
    right_count = Counter(topping)
    left_count = {}

    while index < last_index:
        value = topping[index - 1]
        right_count[value] -= 1
        if right_count[value] == 0:
            del right_count[value]
        if value in left_count:
            left_count[value] +=1
        else:
            left_count[value] = 1
            
        if len(left_count) == len(right_count):
            answer +=1
        index +=1

        
    return answer