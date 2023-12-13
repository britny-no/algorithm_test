# 1025
# 1039

def solution(elements):
    answer = 0
    max_layer = len(elements)
    elements = elements + elements

    s = set([])
    for n in range(1, max_layer + 1):
        start_index = 0
        while start_index < max_layer:
            # print(elements[start_index: start_index + n])
            s.add(sum(elements[start_index: start_index + n]))
            start_index += 1
        
    
    return len(s)