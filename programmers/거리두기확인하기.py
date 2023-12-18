#1431
from collections import deque
import copy

def distance(h,w, H, W):
    return abs(nh-H)+abs(nw-W)

def boundary(nh, nw, H, W):
    return 0<=nh and nh < 5 and 0<= nw and nw < 5 and  (abs(nh-H)+abs(nw-W) <= 2)

def check(p_arr, pre_visited, graph):
    H, W = p_arr
    visited = copy.deepcopy(pre_visited)
    visited[H][W] = True
    
    que = deque([p_arr])
    while que:
        h, w  = que.popleft()
        
        # 상하좌우 왼상대/왼하대 우상대/우하대
        dh = [-1, 1, 0, 0, -1, 1, -1, 1]
        dw = [0, 0, -1, 1, 1, 1, -1, -1]
        
        for i in range(8):
            nh = h + dh[i]
            nw = w + dw[i]
            
            #맨해튼 거리 범위 충족하는지 확인하고 이동  |r1 - r2| + |c1 - c2|
            if boundary(nh, nw, H, W) and visited[nh][nw] == False:
                # 거리두기 조건 미충족시 return False
                
                if graph[h][w] == "P" and graph[nh][nw] == "P":
                    # 상하좌우인데 P일때
                    if i in [0, 1, 2, 3] and graph[h][w] == "O" :
                        # print(h, w, nh, nw,  distance(nh, nw, H, W))
                        return False
                    # 대각선에 있는데 상하좌우에 테이블 있을때
                    # 왼상대/왼하대 우상대/우하대
                    elif i == 4 and ((boundary(nh-1, nw, H, W) and graph[nh-1][nw] == "O") or (boundary(nh, nw-1, H, W) and graph[nh][nw -1] == "O")):
                        # print(h, w, nh, nw,  boundary(nh, nw, H, W))
                        return False
                    elif i == 5 and ((boundary(nh+1, nw, H, W) and graph[nh+1][nw] == "O") or (boundary(nh, nw-1, H, W) and graph[nh][nw -1] == "O")):
                        # print(h, w, nh, nw,  boundary(nh, nw, H, W))
                        return False
                    elif i == 6 and ((boundary(nh-1, nw, H, W) and graph[nh-1][nw] == "O") or (boundary(nh, nw+1, H, W) and graph[nh][nw +1] == "O")):
                        # print(h, w, nh, nw,  boundary(nh, nw, H, W))
                        return False
                    elif i == 7 and ((boundary(nh+1, nw, H, W) and graph[nh+1][nw] == "O") or (boundary(nh, nw+1, H, W) and graph[nh][nw + 1] == "O")):
                        # print(h, w, nh, nw,  boundary(nh, nw, H, W))
                        return False
                        
                else:
                    visited[nh][nw] = True
                    que.append([nh, nw])    
    return True

def solution(places):
    answer = []
    # 두 테이블 T1, T2가 행렬 (r1, c1), (r2, c2)에 각각 위치하고 있다면, T1, T2 사이의 맨해튼 거리는 |r1 - r2| + |c1 - c2| 
    
    # 바로 옆에 있으면 안지킴
    # 맨해튼 거리가 2이하이고 빈테이블이 있으면 안됨
    
    #한 대기실 처리 로직부터 계산

    
    for place in places:
        graph = [['.' for _ in range(5)] for _ in range(5)]
        visited = [[False for _ in range(5)] for _ in range(5)]
        p_arr = []
        for h, row in enumerate(place):
            for w, v in enumerate(row):
                graph[h][w] = v

                if v == "P":
                    p_arr.append([h, w])

        no = False
        for arr in p_arr:
            if check(arr, visited, graph) == False:
                no = True
                break
        # print(place, no)
        if not no :
            answer.append(1)
        else:
            answer.append(0)

    # print(no)
    return answer