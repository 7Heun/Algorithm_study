import sys, math
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
dp = [math.inf] * (k+1)
dp[0] = 0

for i in range(1, k+1):
    for coin in arr:
        if coin > i: continue
        dp[i] = min(dp[i], dp[i - coin] + 1)
print(dp[k] if dp[k] != math.inf else -1)