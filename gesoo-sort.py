arr = [6, 3, 5, 0, 2, 8, 4, 1, 9, 2, 7, 6, 3, 5]
result = ""
# 최대값으로 리스트 0으로 초기화
mainList = [0] * (max(arr) + 1)


#
for i in arr:
  mainList[i] += 1
print(mainList)
for k, i in enumerate(mainList):
  for v in range(i):
    result += " " + str(k)

print(result.strip())
# 0 1 2 2 3 3 4 5 5 6 6 7 8 9