import sys
input = sys.stdin.readline

'''
dp[i]: i번째까지 잔까지 마실 수 있는 최대 양
1. i 안 마심 => dp[i-1]
2. i 마심, i-1 안 마심 => dp[i-2] + wines[i]
3. i 마심, i-1 마심 => dp[i-3] + wines[i-1] + wines[i]
'''

n = int(input())
wines = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n+1)
if n == 1:
    print(wines[1])
    exit()
if n == 2:
    print(wines[1] + wines[2])
    exit()
dp[1] = wines[1]
dp[2] = dp[1] + wines[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-1], dp[i-2] + wines[i], dp[i-3] + wines[i-1] + wines[i])

print(dp[n])