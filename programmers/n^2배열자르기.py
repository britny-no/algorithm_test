def solution(n, left, right):
    answer = []

    left_col = left // n
    left_row = left % n
    right_col = right // n
    right_row = right % n
    
    c = left_col
    r = left_row
    while c < right_col or (c <= right_col and r <= right_row):
        if r > c:
            answer.append(r + 1)
        else:
            answer.append(c + 1)
        
        r +=1
        if r == n :
            c +=1
            r = 0
        
    
        
    return answer