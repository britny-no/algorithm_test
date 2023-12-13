# => 주어진 센서의 위치에 따라, 집중국 위치를 움직일수 있다
# => 센서들은 최소 한개의 집중국과 연결되야하고, 집중국과 센서가 연결된 거리는 최소화시켜야함
# => 센서들은 정수 간격으로 놓일수 있다
# => 센서들은 -1,000,000과 1,000,000사이에 위치할수 있다
# => 센서들의 집중국에 연결된 거리의 합의 최솟값을 구해야한다
# => 집중국의 수신 가능영역의 길이는 0 이상(0일수도 있다)
# => 수신 가능영역의 거리의 합(가능 거리기에, 한 노드에 2개여도 거리는 한개로 본다)

# 애초에 노드에 박는다 생각했는데, 수신 가능 거리라니 실제 거리 계산은 아닌듯...통신 특성을 이용해 센서간 거리를 이용해야할듯
# 명확하지 않고, 애매한 느낌이 있어서 그리드?

# 첫째 줄에 센서의 개수 N(1 ≤ N ≤ 10,000)
# 둘째 줄에 집중국의 개수 K(1 ≤ K ≤ 1000)가 주어진다. 
# 셋째 줄에는 N개의 센서의 좌표가 한 개의 정수로 N개 주어진다. 각 좌표 사이에는 빈 칸이 하나 있으며, 좌표의 절댓값은 1,000,000 이하이다.
import sys

N = int(input())
K = int(input())
SENSOR =  map(int, sys.stdin.readline().split()) # 좌표 리스트
boundary = {}
result = 0

if N>K :
  # 좌표별 갯수 확인
  for i in SENSOR:
    if boundary.get(i):
      boundary[i] +=1
    else:
      boundary[i] = 1

  boundaryArray = sorted(boundary.keys())
  boundaryLen = len(boundaryArray)
  diff = []
  for i in range(0,boundaryLen-1):
    diff.append(boundaryArray[i+1] - boundaryArray[i])
  diff.sort(reverse=True)

  for i in diff[K-1:]:
    result+=i
  print(result)


else:
  print(result)


# for key, value in boundary.items():


