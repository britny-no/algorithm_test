# 2007
# 2052
def generate_bit(n):
    result = ""
    while n > 0:
        result = str(n % 2) + result
        n = n // 2
        
    return result

def return_bit(bit):
    result = 0
    l = len(bit) - 1
    for i, v in enumerate(bit):
        result += 2**(l-i) * int(v)
    return result

def plus_by_bit(bit):
    l = len(bit) - 1
    bit_list = list(bit)
    point = l
    
    up = 1
    while point > -1:
        if up == 1:
            if bit_list[point] == "1":
                up = 1
                bit_list[point] = '0'
            else:
                up = 0
                bit_list[point] = '1'
        point -= 1
    if up == 1:
        bit_list.insert(0, '1')
            
                
    return ''.join(bit_list)

def convert(bit):
    l = len(bit) - 1
    bit_list = list(bit)
    point = l
    for i in range(l, -1, -1):
        if bit_list[i] == "0":
            bit_list[i] = "1"
            bit_list[i+1] = "0"
            break
    return ''.join(bit_list)

def solution(numbers):
    answer = []
    for n in numbers:   
        if n % 2 == 1:
            bit = generate_bit(n)
            if '0' in bit:
                answer.append(return_bit(convert(bit)))
            else:
                answer.append(return_bit(convert("0"+bit)))
        else:
            answer.append(n+1)

    return answer