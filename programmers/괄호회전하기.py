import re

def check(s):
    text = '[1](){3}()'
    l = len(s) -1 
    c = 0

    while s != "" and c <= l:
        s = re.sub('(\(\))|(\[\])|(\{\})', "" , s)
        c+=1
    
    return True if s == "" else False
    
    
def solution(s):
    answer = 0
    l = len(s) - 1
    c = 0

    if check(s):
        answer +=1
        
    while c < l:
        string = s[0]
        s = s[1:]
        s += string
        if check(s):
            answer +=1
        c +=1

    
    return answer