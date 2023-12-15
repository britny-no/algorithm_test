def solution(word):
    global answer 
    answer = 0
    arr = ['A', 'E', 'I', 'O', 'U']
    
    def dfs(string):
        global answer
        answer+=1
        # print(string)
        if string == word:
            return True
        
        if len(string) == 5:
            return False
        
        for i in arr:
            if dfs(string + i) == True:
                return True
            
    for i in arr:
        # global answer
        if dfs(i) == True:
            return answer
        
        
    return answer