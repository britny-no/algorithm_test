from collections import Counter

def solution(people, limit):
    answer = 0
    counter = Counter(people)
    counter_keys = sorted(counter.keys())
    total = sum(counter.values())
    
    while total > 0 and counter_keys:
        s = 0
        local_count = 0
        cur_kg = 0
        while s < limit and  counter_keys:
            key = counter_keys[-1]
            if counter[key] > 0:
                cur_kg = key
                s += key
                counter[key]  -= 1
                local_count +=1
            elif counter[key] == 0:
                counter_keys = counter_keys[:-1]
                
        
        if s > limit:
            s += cur_kg
            counter[cur_kg] +=1
            local_count -=1
            
        total -= local_count
        answer +=1
            
            
        
                
        
    # print(counter_keys)
    

        
    return answer