# 1341
from itertools import combinations, permutations
import re
import copy

def solution(expression):
    answer = 0
    number_arr = re.compile('[0-9]+').findall(expression)
    operator_arr = re.compile('[/+/*/-]').findall(expression)
    operator_set = list(set(operator_arr))
    combi = list(permutations(operator_set, len(operator_set)))
    
    # 우선순위에 따라 계산
    for case in combi:
        local_number_arr = copy.deepcopy(number_arr)
        local_operator_arr = copy.deepcopy(operator_arr)
        for op in case:
            while op in local_operator_arr:
                pos = local_operator_arr.index(op)
                sum_v = 0
                if op == "-":
                    sum_v = int(local_number_arr[pos]) - int(local_number_arr[pos+1])
                elif op == '+':
                    sum_v = int(local_number_arr[pos]) + int(local_number_arr[pos+1])
                else:
                    sum_v = int(local_number_arr[pos]) * int(local_number_arr[pos+1])
                del local_operator_arr[pos]
                del local_number_arr[pos]
                local_number_arr[pos] = sum_v
        answer = max(answer, abs(int(local_number_arr[0])))
            
    # 최대 계산값 도출
    return answer