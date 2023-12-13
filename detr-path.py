
# '무한'을 의미하는 값으로 10억을 활용
INF = int(1e9)

# 노드와 간선의 개수를 각각 입력받기
n, e = map(int, input().split())

# 시작 노드 번호를 입력받기
start = int(input())
graph = [[] for i in range(n+1)]
# print([[] for i in range(n+1)])
# print([[]] * (n+1)) 파이썬 배열에서 *은 반복문보단 증가에 가깝다

# 간선 그래프 생성
# e가 왜 필요? e 갯수만큼 for문 돌려야하네
for i in range(e):
  startNode, tarNode, distance = map(int, input().split())
  graph[startNode].append((tarNode, distance))

# 방문 여부
visited = [False] * (n + 1)
visited[0] = True

resultList = [INF] * (n+1)
resultList[start] = 0

print('??')
print(graph)

def minNonVisited(array, visited):
  nonVisit = [i for i, value in enumerate(visited) if value == False]
  return [array[v] for v in nonVisit]

while False in visited:
  # 가장 최소 값중 방문 안한 노드 검색
  # 방문을 안한 놈들중 최소값을 찾아야함
  print(visited, minNonVisited(resultList, visited), resultList)
  for i, v in enumerate(resultList):
    if v == min(minNonVisited(resultList, visited)) and visited[i] == False:
      visited[i] = True

      # 간선들 정보 가져온다
      for tarNode, d in graph[i]:
        if v + d < resultList[tarNode]:
          resultList[tarNode] = v + d


print(resultList)



  

# 노드와 간선의 개수를 각각 입력하세요: 6 13
# 시작 노드를 설정하세요: 1
# 1 2 2
# 1 4 1
# 1 5 3
# 2 3 3
# 2 6 2
# 3 2 3
# 4 3 1
# 4 5 3
# 5 2 5
# 5 3 2
# 6 3 5
# 6 4 4
# 6 5 1


# 최단 거리 리스트, 노드 방문 여부, 간선 그래프