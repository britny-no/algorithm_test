def return_u_v(p):
    u = ""
    ob = {
        '(': 0,
        ')': 0
    }
    count = 0
    while p:
        if count > 0 and count % 2 == 0 and ob['('] == ob[')']:
            break
        value = p[0]
        ob[value] +=1
        u +=value
        p = p[1:]
        count +=1
    v = p
    
    return [u, p]

def check_allbaron(tar):
    l = len(tar)
    count = 0
    while count <= l//2:
        tar = tar.replace('()', '')
        count +=1
    return tar

def convert(tar):
    result = ""
    for i in tar:
        if i == "(":
            result += ")"
        else:
            result += "("
    return result

def process(w):
    if w == "":
        return w
    else:
        u, v = return_u_v(w)
        if check_allbaron(u) == "":
            return u + process(v)
        else:
            return "(" + process(v) + ")" + convert(u[1: -1])
            
    
def solution(p):
    return process(p)