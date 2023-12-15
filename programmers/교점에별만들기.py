# 1354
from itertools import *
# 모든 직선간 교점 Or 평행/일치 여부 부터

def solution(line):
    answer = []
    point = []
    max_up = None
    max_down = None
    max_left = None
    max_right = None
    
    for arr1, arr2 in list(combinations(line, 2)):
        A, B, E = arr1
        C, D, F = arr2
        if A*D - B*C != 0:
            x = (B*F - E*D)/(A*D - B*C)
            y = (E*C - A*F)/(A*D - B*C)
            x_int = int(x)
            y_int = int(y)
            if x == x_int and y == y_int:
                point.append((x_int, y_int))
                if max_up == None:
                    max_up = y_int
                else:
                    max_up = max(max_up, y_int)
                
                if max_down == None:
                    max_down = y_int
                else:
                    max_down = min(max_down, y_int)
                
                if max_right == None:
                    max_right = x_int
                else:
                    max_right = max(max_right, x_int)
                    
                if max_left == None:
                    max_left = x_int
                else:
                    max_left = min(max_left, x_int)

    if max_up == None:
        max_up = max_down
    if max_down == None:
        max_up = max_up
    if max_right == None:
        max_right = max_left
    if max_left == None:
        max_left = max_right
        
    if max_up == 0 and max_down == 0 and max_right == 0 and max_left == 0:
        return ['*']

    for h in range(max_down, max_up +1, 1):
        r = ""
        for w in range(max_left, max_right + 1, 1):
            if (w, h) in point:
                r+="*"
            else:
                r+="."
        answer.insert(0, r)
    return answer