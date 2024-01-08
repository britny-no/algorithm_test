def solution(record):
    answer = []
    result = []
    nickname_ob = {}
    direct_ob = {
        'Enter': '들어왔습니다',
        'Leave': '나갔습니다'
    }
    
    for string_arr in record:
        arr = string_arr.split(' ')
        
        if len(arr) == 3:
            nickname_ob[arr[1]] = arr[2]
        
    
        if arr[0] != "Change":
            answer.append(arr[1]+"님이 "+direct_ob[arr[0]]+".")
    
    for tar in answer:
        uid, rest = tar.split('님')
        result.append(nickname_ob[uid]+'님'+rest)
    
    
    
    return result