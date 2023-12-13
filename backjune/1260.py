# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 
# 정점 번호는 1번부터 N번까지이다.

# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 


import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 
# 입력으로 주어지는 간선은 양방향이다
for _ in range(M):
  Node1, Node2 = map(int, sys.stdin.readline().split())
  graph[Node1].append(Node2) #우선순위 큐 사용도 가능
  graph[Node2].append(Node1)


# 작은값부터 진행해야하니, 오름차순 정렬 되어있어야함
for i in graph:
  i.sort()


# DFS 스택, BFS 큐

def DFS(start_node):
  result = str(start_node)
  visited = [False for _ in range(N+1)]
  visited[0] = True

  stack = [start_node]
  visited[start_node] = True

  while stack:
    target_node = stack[-1]

    if graph[target_node]:
      check_count = 0

      for node in graph[target_node]:
        if visited[node] == False:
          result += " " + str(node)
          visited[node] = True
          stack.append(node)
          break
        else:
          check_count += 1

      if check_count == len(graph[target_node]):
        stack.pop()
    else:
      stack.pop()

  # 연결 안된 접점 표기
  # while False in visited:
  #   target_node = visited.index(False)
  #   visited[target_node] = True
  #   result += " "+ str(target_node)

  return result.strip()


def BFS(start_node):
  result = str(start_node)
  visited = [False for _ in range(N+1)]
  visited[0] = True

  que = deque([start_node])
  visited[start_node] = True

  while que:
    target_node = que.popleft()

    for child_node in graph[target_node]:
      if visited[child_node] == False:
        result += " " + str(child_node)
        visited[child_node] = True
        que.append(child_node)

  # 연결 안된 접점 표기
  # while False in visited:
  #   target_node = visited.index(False)
  #   visited[target_node] = True
  #   result += " "+ str(target_node)

  return result.strip()
  

# DFS/BFS 각각 출력 해야함
print(DFS(V))
print(BFS(V))
