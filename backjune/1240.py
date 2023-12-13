# 1240문제

# from collections import deque
# import copy

# graph = [
#     [],
#     [[2, 2], [4, 3]],
#     [[1, 2]],
#     [[4, 2]],
#     [[3, 2], [1, 3]],
# ]

# # visited = [False] * len(graph)

# # bfs, dfs 둘중 아무거나 써도 됨
# def bfs(visited, start, end):
#   # local_graph = copy.deepcopy(graph)
#   que = deque([[start, 0]])
#   visited[start] = True

#   while que:
#     node_num, d_v = que.popleft()

#     if node_num == end:
#       return d_v
    
#     for i, i_d_v in graph[node_num]: #조금 더 섬세히 하면, 인접 노드중 작은 놈부터 처리
#       if visited[i] == False:
#         visited[i] = True
#         que.append([i, d_v+i_d_v])

# print(bfs([False] * len(graph), 1, 2))
# print(bfs([False] * len(graph), 3, 2))







  