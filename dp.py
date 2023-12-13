# 재귀 함수
def f(n):
  if n == 1 or n == 2:
    return 1
  return f(n-1)+f(n-2)


# print(f(4))

# 탑다운(메모제이션 사용)
n = 10
memo = [0] * (n + 1)

def topDown(n):
  if n == 1 or n == 2:
    return 1
  memo[n] = f(n-1)+f(n-2)
  return memo[n]


# bottom up

def bottomUp(n):
  memo[1] = 1
  memo[2] = 1
  for i in range(3, n+1):
      memo[i] = memo[i-1] + memo[i-2]

  return memo[n]

  

print(bottomUp(4))
