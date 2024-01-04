#1033
def solution(n):
    answer = []
    graph = [[0] * _ for _ in range(1, n+1)]
    start_layer = 0
    end_layer = n - 1
    start_plus = 0
    end_minus = 0
    
    
    i = 1
    status_1 = True
    status_2 = True
    status_3 = True
    while status_1 or status_2 or status_3:
        start_i  =  i
        for h in range(start_layer, end_layer + 1):
            w = start_plus
            if graph[h][w] == 0:
                graph[h][w] = i
                i += 1
        status_1 = start_i  != i
        start_plus += 1
        start_layer += 1
        
        start_i  =  i
        for index, v in enumerate(graph[end_layer][start_plus:h - end_minus + 1]):
            if graph[end_layer][index+start_plus]  == 0:   
                graph[end_layer][index+start_plus] = i 
                i+=1
        status_2 = start_i  != i
        end_layer -= 1
        
        start_i  =  i
        for h in range(end_layer, start_layer - 1, -1):
            w = h - end_minus
            if graph[h][w] == 0:
                graph[h][w] = i
                i += 1
        status_3 = start_i  != i
        end_minus +=1
    
    for i in graph:
        answer += i
    
    
    return answer