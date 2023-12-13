# 1228

# 우리 병사와 적국 병사가 섞여 싸우게 되었다. 
# 당신의 병사들은 흰색 옷을 입고, 적국의 병사들은 파란색 옷을 입었기 때문에 서로가 적인지 아군인지는 구분할 수 있다. 
# 문제는 같은 팀의 병사들은 모이면 모일수록 강해진다는 사실이다.
# N명이 뭉쳐있을 때는 N2의 위력을 낼 수 있다. 
# 과연 지금 난전의 상황에서는 누가 승리할 것인가? 단, 같은 팀의 병사들이 대각선으로만 인접한 경우는 뭉쳐 있다고 보지 않는다.

# 입력
# 첫째 줄에는 전쟁터의 가로 크기 N, 세로 크기 M(1 ≤ N, M ≤ 100)이 주어진다. 
# 그 다음 두 번째 줄에서 M+1번째 줄에는 각각 (X, Y)에 있는 병사들의 옷색이 띄어쓰기 없이 주어진다. 
# 모든 자리에는 병사가 한 명 있다. -> 전쟁터를 꽉 채운다
# B는 파란색, W는 흰색이다. 
# 당신의 병사와 적국의 병사는 한 명 이상 존재한다. -> 한명 이상 존재한다

# 출력
# 각국 병사의 위력의 합을 출력하라






import sys
from collections import deque

WIDTH, HEIGHT = map(int, sys.stdin.readline().split())

# 동서남북 4 방향으로 붙어있을때 그룹화 할수 있고, 이때 위력이 N제곱으로 계산된다
# 안 뭉쳐있으면 그냥 +1 혹은 +N

# 위치별 W, B부텉 정리
graph = [[] for _ in range(HEIGHT+1)] #IndexError 방지차 +1
checked = [[False for _ in range(WIDTH)] for _ in range(HEIGHT)]

# 입력 모양 그대로 전투장 배열화
for h in range(HEIGHT):
  width = input()
  for v in width:
    graph[HEIGHT-h-1].append(v)


# bfs que 사용
def landScan(start, end):
  que = deque([(start, end)])
  checked[start][end] = True
  result = []
  bias_team = graph[start][end]

  while que:
    h, w = que.popleft()
    result.append((h, w))
    # B인지 W인지 판단
    team = graph[h][w]
    
    # 위로 이동
    while (0 <= h+1 and h+1 < HEIGHT) and (0 <= w and w < WIDTH) and team == graph[h+1][w] and checked[h+1][w] == False:
      checked[h+1][w] = True
      que.append((h+1, w))
      break
    # 아래로 이동
    while (0 <= h - 1 and h - 1 < HEIGHT) and (0 <= w and w < WIDTH) and team == graph[h-1][w] and checked[h-1][w] == False:
      checked[h-1][w] = True
      que.append((h-1, w))
      break
    # 우측으로 이동
    while (0 <= h and h < HEIGHT) and (0 <= w + 1 and w + 1 < WIDTH) and team == graph[h][w+1] and checked[h][w+1] == False:
      checked[h][w+1] = True
      que.append((h, w+1))
      break
    # 좌측으로 이동
    while (0 <= h and h < HEIGHT) and (0 <= w - 1 and w - 1 < WIDTH) and team == graph[h][w-1] and checked[h][w-1] == False:
      checked[h][w-1] = True
      que.append((h, w-1))
      break
  
  return [bias_team, result]

B_result = 0
W_result = 0
# checked 없는 애들중 width 가장 작은 놈

for h in range(len(graph)):
  for w, v in  enumerate(graph[h]):
    if checked[h][w] == False:
      team, result = landScan(h, w)
      if team == "B":
        B_result += len(result)**2
      else:
        W_result += len(result)**2


print(W_result, B_result)


    


