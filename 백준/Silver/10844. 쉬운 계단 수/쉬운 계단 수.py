import sys
input = sys.stdin.readline

n = int(input())
MOD = 1000000000

# dp[i][j]: i자리 수 중 j 로 끝나는 계단 수의 개수
dp = [[0] * 10 for _ in range(n+1)]
dp[1] = [0] + [1] * 9

for i in range(2, n+1):
    # 0으로 끝나는 경우
    dp[i][0] = dp[i-1][1]
    # 9로 끝나는 경우
    dp[i][9] = dp[i-1][8]
    # 1~8로 끝나는 경우
    for j in range(1, 9):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % MOD

print(sum(dp[n]) % MOD)