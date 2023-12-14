# 1405
# 1423

from collections import Counter

def compare_ob(ob1, ob2):
    for key in ob1:
        if ob2[key]:
            ob2[key] -=ob1[key]
            
            if ob2[key] < 0 :
                return False
            elif ob2[key] == 0:
                del ob2[key]
        else:
            return False
        
    if len(ob2) > 0:
        return False
    else:
        return True
    
def solution(want, number, discount):
    answer = 0
    want_ob = {}
    want_len = len(want)
    discount_len = len(discount)
    
    
    for i in range(want_len):
        want_ob[want[i]] = number[i]
    
    
    for i in range(discount_len-9):
        if compare_ob(want_ob, Counter(discount[i: i + 10])):
            answer += 1
    
    return answer