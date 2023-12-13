# 이진 탐색은 정렬된 정수 리스트에서 유효

a = [1, 2, 3, 4,5,6,7,8,9,20]


def binarySearch(array, findValue):
  startIndex = 0
  endIndex = len(array) - 1
  middleIndex = startIndex+((endIndex-startIndex)//2)

  # print(array.index(findValue))

  # 두 조건문 모두 가능. 다만, 값으로 조건 주면 값이 없는 경우 고려해야함.
  # 인덱스 크기로 조건주면 값 없으면 그냥 근사 인덱스 리턴
  while findValue != array[middleIndex]: 
  # while startIndex < endIndex:
    middleIndex = startIndex+((endIndex-startIndex)//2)

    if findValue > array[middleIndex]:
      startIndex = middleIndex + 1
    elif findValue < array[middleIndex]:
      endIndex = middleIndex - 1
    else:
      print(middleIndex)
      break

  return array[middleIndex]
      


print(binarySearch(a, 21))