#1829
# 1904

def solution(dirs):
    answer = 0
    visited = [[[] for _ in range(11)] for _ in range(11)]
    
    move_ob = {
        'U': [1, 0],
        'D': [-1, 0],
        'L': [0, -1],
        'R': [0, 1]
    }
    pre_pos = [5, 5]
    
    for di in dirs:
        h, w = pre_pos
        nh, nw = move_ob[di]
        dh = h + nh
        dw = w + nw
        
        if dh < 0 or 10 < dh or dw < 0 or 10 < dw:
            continue
        else:
            pre_pos = [dh, dw]
            if [dh, dw] in visited[h][w]:
                continue
            else:
                answer +=1
                visited[h][w].append([dh, dw])
                visited[dh][dw].append([h, w])
                
            
                
                
    
    return answer