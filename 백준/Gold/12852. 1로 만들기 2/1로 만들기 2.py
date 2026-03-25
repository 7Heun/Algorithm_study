import sys
input = sys.stdin.readline

'''
dp[1]에서 dp[n]까지
prev 배열 만들어서 경로 역추적
'''
n = int(input())
dp = ['inf'] * (n+1)
dp[1] = 0
prev = [0] * (n+1)

for i in range(2, n+1):
    cases = [(dp[i-1] + 1, i-1)]
    if i % 2 == 0:
       cases.append((dp[i//2] + 1, i//2))
    if i % 3 == 0:
        cases.append((dp[i//3] + 1, i//3))
    dp[i], prev[i] = min(cases)

path = []
cur = n
while cur > 0:
    path.append(cur)
    cur = prev[cur]

print(dp[n])
print(*path)