# sort 쓸수도 있음
from collections import deque

# 가장 큰 값 뽑는게 나을듯
def sortFunc(array):
  biggest = 0

  for i in array:
    if i > biggest:
      biggest = i
  return biggest
  
array = [2, 3, 1, 5]
que = deque()

while array:
  biggest = sortFunc(array)
  que.appendleft(biggest)
  array.remove(biggest)

print(que)
