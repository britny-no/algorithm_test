def check_consecutive(s, degree):
    result = ""
    
    pre_value = ""
    value = ""
    consecutive_count = 0

    
    #초기화
    value = s[0: degree]
    s = s[degree: ]
    pre_value = value
    consecutive_count = 1
    
    while s:
        value = s[0: degree]
        s = s[degree: ]
            
        if value != pre_value:
            if consecutive_count == 1:
                result += pre_value
            else:
                result += str(consecutive_count)+pre_value

            consecutive_count = 1
        else:
            consecutive_count +=1
            
        pre_value = value
    
    # 마지막
    if consecutive_count == 1:
        result += pre_value
    else:
        result += str(consecutive_count)+pre_value
                
                
    
            
    return result

def solution(s):
    answer = 1000
    for i in range(1, len(s) + 1):
        sub_answer = check_consecutive(s, i)
        answer = min(len(sub_answer), answer)
        
    return answer