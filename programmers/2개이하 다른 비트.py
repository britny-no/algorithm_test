# 2007

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

def check_diff(bit1, bit2):
    l1 = len(bit1)
    l2 = len(bit2)
    range_l = 0
    
    if l1 > l2:
        while l1 != l2:
            bit2 = '0' + bit2
            l2 = len(bit2)
    elif l1 < l2:
        while l1 != l2:
            bit1 = '0' + bit1
            l1 = len(bit1)
        
    count = 0
    for i in range(l1):
        if bit1[i] != bit2[i]:
    # print('count', count, bit1, bit2)
            
    return True if count > 2 else False

def solution(numbers):
    answer = []
    for n in numbers:   
        start_bit = generate_bit(n)
        n+=1
        next_bit = generate_bit(n)
    
        while check_diff(start_bit, next_bit):
            n+=1
            # print(n)
            next_bit = generate_bit(n)
        # print(1123,n)
        answer.append(n)
    # print(generate_bit(n), return_bit(generate_bit(n)))
    
    return answer