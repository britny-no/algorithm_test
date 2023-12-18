#1431
from collections import deque
import copy

def boundary(nh, nw, H, W):
    return 0<=nh and nh < 5 and 0<= nw and nw < 5 and  (abs(nh-H)+abs(nw-W) <= 2)

def check(p_arr, graph):
    H, W = p_arr
    h, w = p_arr

    # 상하좌우 왼상대/왼하대 우상대/우하대
    dh = [-1, 1, 0, 0, -1, 1, -1, 1]
    dw = [0, 0, -1, 1, 1, 1, -1, -1]

    for i in range(8):
        nh = h + dh[i]
        nw = w + dw[i]

        #맨해튼 거리 범위 충족하는지 확인하고 이동  |r1 - r2| + |c1 - c2|
        if boundary(nh, nw, H, W):
            # 거리두기 조건 미충족시 return False
            if i in [0, 1, 2, 3]:
                if graph[nh][nw] == "P":
                    return False
                elif graph[nh][nw] == "O" and boundary(nh+dh[i], nw+dw[i], H, W) and graph[nh+dh[i]][nw+dw[i]] == "P":
                    return False
            else:
                if graph[nh][nw] == "P":  
                    if i == 4 and ((boundary(nh-1, nw, H, W) and graph[nh-1][nw] == "O") or (boundary(nh, nw-1, H, W) and graph[nh][nw -1] == "O")):
                        return False
                    elif i == 5 and ((boundary(nh+1, nw, H, W) and graph[nh+1][nw] == "O") or (boundary(nh, nw-1, H, W) and graph[nh][nw -1] == "O")):
                        return False
                    elif i == 6 and ((boundary(nh-1, nw, H, W) and graph[nh-1][nw] == "O") or (boundary(nh, nw+1, H, W) and graph[nh][nw +1] == "O")):
                        return False
                    elif i == 7 and ((boundary(nh+1, nw, H, W) and graph[nh+1][nw] == "O") or (boundary(nh, nw+1, H, W) and graph[nh][nw + 1] == "O")):
                        return False

 
    return True

def solution(places):
    answer = []
    
    for place in places:
        graph = [['.' for _ in range(5)] for _ in range(5)]
        p_arr = []
        for h, row in enumerate(place):
            for w, v in enumerate(row):
                graph[h][w] = v

                if v == "P":
                    p_arr.append([h, w])

        no = False
        for arr in p_arr:
            if check(arr, graph) == False:
                no = True
                break
        if not no :
            answer.append(1)
        else:
            answer.append(0)

    return answer