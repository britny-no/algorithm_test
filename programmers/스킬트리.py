from collections import Counter
import copy

def solution(skill, skill_trees):
    answer = 0
    counter = Counter(skill)
    
    
    for skills in skill_trees:
        answer +=1
        local_skill = skill
        local_counter = copy.deepcopy(counter)
        
        for ski in skills:
            if ski in local_counter and local_counter[ski] > 0:
                if len(local_skill) > 0:
                    if local_skill[0] == ski:
                        local_skill = local_skill[1:]
                        local_counter[ski] -= 1
                    else:
                        answer -=1
                        break
                
            
            
        
        
    return answer