def arr_split(arr, next_n):
    fisrt = []
    second = []
    
    for a in arr:
        fisrt.append(a[0: next_n])
        second.append(a[next_n: ])
    return [fisrt, second]
    
    
def solution(arr):
    answer = [0, 0]
    
    def check_unity(arr):
        H = len(arr)
        W = H

        if H == 1:
            answer[arr[0][0]] +=1
            return 
        else:
            for h in range(H):
                for w in range(W):
                    if arr[h][w] != arr[0][0]:
                        next_n = H//2

                        first, second = arr_split(arr[0: next_n], next_n)
                        first2, second2 = arr_split(arr[next_n:], next_n)
                        check_unity(first)
                        check_unity(second)
                        check_unity(first2)
                        check_unity(second2)

                        return

            answer[arr[0][0]] += 1
        return 
        
        
    check_unity(arr)
    
    return answer