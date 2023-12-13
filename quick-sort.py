from collections import deque



# -방문 여부, 리스트 쪼갠 여부, 마지막 작은 값(마지막 small인지, 남았는데 small인지) 위치를 알아야할듯

array = [5, 8, 0, 9, 6, 1, 2, 4, 7, 3]
count = len(array)

def quickMain(array):
  pivot = array[0]
  print('@@@@@@@@@@@ pivot @@@@@@@@@@@', pivot)

  visited = [False] * (len(array))
  visited[0] = True
  lastPivotIndex = 0

  while (False in visited):
    # 좌측부터 피봇보다 큰놈
    big = -1
    small = -1
    for i, v in enumerate(array[1: len(array)]):
      if visited[i+1] == False and v > pivot:
        big = v
        visited[i+1] = True
        break
      else:
        visited[i+1] = True
      


    # 우측부터 피봇보다 작은
    for i, v in enumerate(reversed(array[1: len(array)])):
      if visited[len(array)-1-i] == False and v < pivot:
        small = v
        visited[len(array)-1-i] = True
        break
      else:
        visited[len(array)-1-i] = True

    if big != -1 and small != -1:
      bigIndex = array.index(big)
      smallIndex = array.index(small)
      array[bigIndex] = small
      array[smallIndex] = big

      # 엇갈릴때 오른쪽의 값과 피봇을 스왑 하는데, 그걸 깔끔하게 while로 구현해보자
      # 사이에 값 한개일 경우
      # 피봇보다 작으면 피봇과 스왑, 크면 그 앞에 두기
      if visited.count(False) == 1:
        tarIndex = visited.index(False)
        tarValue = array[tarIndex]
        if tarValue < pivot:
          array[0] = tarValue
          array[tarIndex] = pivot
          visited[tarIndex] = True
          lastPivotIndex= tarIndex
        else:
          array.remove(pivot)
          array.insert(tarIndex - 1, pivot)
          visited[tarIndex] = True
          lastPivotIndex= tarIndex - 1
      # 사이에 값 없을 경우
      # 마지막 값중 작은 값과 스왑
      elif visited.count(False) == 0:
        tarIndex = array.index(small)
        tarValue = array[tarIndex]
        array[0] = tarValue
        array[tarIndex] = pivot
        lastPivotIndex= tarIndex 
  return [array, lastPivotIndex]



def quickSort(array, start, end):
  # 퀵 정렬 구조를 봤을때, 완탐이 가능하다 생각. 하지만, 엇갈린 경우를 고려하면 완탐 미 사용
  # 엇갈림을 구현할수 있어야하고, 스와프된 지점에서 시작되야하기에 visited보단 인덱스 값 갱신으로 접근
  if start >= end: 
    return
      
  pivot = start
  left = start + 1
  right = end

  while left <= right: # 엇갈린 경우 멈춰야한다
    # 좌측에서 피봇 보다 큰놈 찾는다
    while left <= end and array[left] <= array[pivot]:
      left += 1 # 큰놈 찾기 위해, 작거나 같은놈이면 계속 증가시킨다
    
    while right > start and array[right] >= array[pivot]:
      right -= 1
    
    # 엇갈렸으면 오른쪽 값과 피봇 변경
    if left > right:
      array[pivot], array[right] =  array[right], array[pivot]
    else :
      array[left], array[right] =  array[right], array[left]
    
  
  # 좌/우측 정렬시 피봇 기준이 맞는데, 정확히는 직전 정렬(분할)중 right에 담긴 인덱스 기준임
  quickSort(array, 0, right - 1)
  quickSort(array, right + 1, end)


quickSort(array, 0, len(array)-1)
print(array)

# array, lastPivotIndex = quickMain(array)
# # 왼쪽 
# leftStart = 0
# leftPivot = lastPivotIndex
# leftArray = array[leftStart: leftPivot]
# leftResult = []

# while leftArray:
#   if len(leftArray) > 1:
#     array2, lastPivotIndex2 = quickMain(leftArray)
#     if lastPivotIndex2 == 1 and min(array2) == array2[0]: #첫 요소가 가장 작고, pivot 인덱스가 1일때 왼쪽 결정
#       leftStart = lastPivotIndex2+ 1
#       leftArray = array2[leftStart: ]

#       for i in array2[0: lastPivotIndex2+1]:
#         leftResult.append(i)
#   else:
#     leftResult.append(leftArray[0])
#     leftArray = []


# # 오른쪽
# rightStart = lastPivotIndex+1
# rightPivot = len(array)
# rightArray = array[rightStart: rightPivot]
# rightResult = []

# while rightArray:
#   if len(rightArray) > 1:
#     array2, lastPivotIndex2 = quickMain(rightArray)
#     if lastPivotIndex2 == 1 and min(array2) == array2[0]: #첫 요소가 가장 작고, pivot 인덱스가 1일때 왼쪽 결정
#       leftStart = lastPivotIndex2+ 1
#       rightArray = array2[leftStart: ]

#       for i in array2[0: lastPivotIndex2+1]:
#         leftResult.append(i)
#   else:
#     leftResult.append(rightArray[0])
#     rightArray = []
# print(rightResult)
# # array3, lastPivotIndex3 = quickMain(rightArray)
# # print(array3)