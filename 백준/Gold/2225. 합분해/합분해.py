import sys
input = sys.stdin.readline

'''
dp[i][j]: i를 j개로 만드는 경우의 수
1. (~~) + 0: dp[i][j-1]
2. 그 외: dp[i-1][j]
dp[i][j] = dp[i][j-1] + dp[i-1][j]
'''

n, k = map(int, input().split())
dp = [[0] * (k+1) for _ in range(n+1)]
MOD = 1000000000

for i in range(1, n+1):
    dp[i][1] = 1

for j in range(1, k+1):
    dp[0][j] = 1

for i in range(1, n+1):
    for j in range(1, k+1):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % MOD

print((dp[n][k]) % MOD)

