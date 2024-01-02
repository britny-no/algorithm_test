def conversion(l):
    l = int(l)
    result = ""
    
    while l > 0:
        result = str(l % 2) + result
        l = l // 2 
    return result
        
def solution(s):
    answer = []
    count = 0
    zero_count = 0
    
    
    while s != "1":
        origin_l = len(s)
        s = s.replace('0', '')
        l = len(s)

        zero_count+= origin_l-l
        count+=1
        
        s = conversion(l)
        
        
    return [count, zero_count]