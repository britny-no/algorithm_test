from collections import deque

graph = [
    [],
    [2, 3],
    [1, 8],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7, 8],
    [6, 8],
    [2, 6, 7]
]

visited = [False] * len(graph)

def bfs(graph, node, visited): #node는 시작 노드. 트리의 루트는 있지만, 루트는 정해져있다 생각하지 말자
  que = deque([node])
  visited[node] = True

  while que:
    node_num = que.popleft()
    print(node_num)
    for i in graph[node_num]: #조금 더 섬세히 하면, 인접 노드중 작은 놈부터 처리
      if visited[i] == False:
        visited[i] = True
        que.append(i)
# bfs(graph, 4, visited)

def dfs(graph, node, visited):
  # 비재귀 함수 버전
  # stack = [node]
  # visited[node] = True
  # print(node)
  # while stack:
  #   node_num = stack[-1] #pop과 다르게 맨위 값을 가져오기만 함
  #   visited[node_num] = True
  #   if graph[node_num]:
  #     # 제일 작고 방문하지 않은 노드 설정해야함. 없으면 
  #     # 제일 작은 조건 필요시 sort 사용하는데, 시작전 전체 sort 가정
  #     none_target_count = 0
  #     for i in graph[node_num]:
  #       if visited[i] == False:
  #         visited[i] = True
  #         stack.append(i)
  #         print(i)
  #         break
  #       else:
  #         none_target_count += 1

  #       if none_target_count == len(graph[node_num]):
  #         stack.pop()
  #   else:
  #      stack.pop()

    # 재귀 함수 버전
    stack = [node]
    visited[node] = True
    print(node)
    none_target_count = 0
    for i in graph[node]:
      if visited[i] == False:
        dfs(graph, i, visited)
      else:
        none_target_count += 1

    if none_target_count == len(graph[node]):
        stack.pop()
      

# dfs(graph, 1, visited)
# 1 -> 2 -> 8 -> 6 -> 7 -> 3 -> 4 -> 5






        
