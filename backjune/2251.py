import sys
from collections import deque

# 입력(리터 범위)
a, b, c = map(int, sys.stdin.readline().split())


# A, B, C의 물통 크기를 a, b, c
# A, B, C에 각 들어있는 물의 양을 x, y, z
# 경우의 수중 x = 0일때 z의 케이스들 오름차순으로 출력해라

# 모든 경우의 수를 확인해야한다  -> 완전 탐색 해야한다 -> BFS 사용
# 그래프가 없다 어떻게? 한개의 (x,y,z)를 노드로, 가지를 뻗혀간다 생각하면 된다
# visited로 확인한 케이스 재확인 방자
# 손으로 짜보니 이동 물의 양이 0일때는, 변화가 없으므로 굳이 visited 처리 안해도 된다


# a * b로 2차원 배열의 visited 생성
# visited =  [[False] * (b+1)] * (a+1) # 왜 안되지?
visited = [[False] * (b+1) for _ in range(a+1)]



# bfs이니 큐 사용
que = deque([(0, 0)])
visited[0][0] = True
answer = []

def check(x, y):
  if visited[x][y] == False:
    visited[x][y] = True
    que.append((x, y))

while que:
  x, y = que.popleft()
  z = c - x - y

  if x == 0:
    answer.append(z)

  #완탐은 한가지 행위?별로 모두 확인하니 x -> y, x -> z를 가지로 생각
  # x -> y
  water = min(x, b - y) #a를 비우거나, b를 채우거나
  # 옮길때 넘치는 경우 염려해, 현재 가진 물과 옮길 물통을 채울 물중 작은 놈으로 옮길 물 결정
  if water > 0: # if문 성능이슈시 주석
    check(x - water, y + water)
  
  # x -> z
  water = min(x , c - z)
  if water > 0:
    check(x-water, y)

  # y - > x
  water = min(y , a - x)
  if water > 0:
    check(x + water, y - water)
  
  # y -> z
  water = min(y , c - z)
  if water > 0:
    check(x, y - water)

  # z -> x
  water = min(z , a - x)
  if water > 0:
    check(x + water, y)

  # z -> y
  water = min(z , b - y)
  if water > 0:
    check(x , y+water)

answer.sort()
result = ""
for i in answer:
  result+= " "+str(i)
print(result.lstrip())

