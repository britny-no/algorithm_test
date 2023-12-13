from collections import deque
from queue import PriorityQueue
import copy
# 입력 순서와 상관없이, 작은 놈부터 pop하는 큐

# 앞에 정렬 시키는 놈

array = [7, 1, 20, 2, 19, 4, 5]
result = [array[0]]


def insertFunc(result, target):
  # result는 정렬되어 있다
  returnResult = copy.deepcopy(result)
  insertIsit = False
  for i, v in enumerate(returnResult):
    if v > target:
      returnResult.insert(i, target)
      insertIsit = True
      break
  
  if insertIsit == False:
    returnResult.append(target)


  return returnResult


for v in  array[1: len(array)]:
  # result에서 적적한 위치 찾아서 삽입
  result = insertFunc(result, v)

print(result)


