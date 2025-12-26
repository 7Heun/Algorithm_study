import sys
input = sys.stdin.readline


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

'''
dp[i][j]: 행렬 i ~ 행렬 j를 곱한 것의 최소 연산 횟수 (i <= j)
모든 k(i <= k < j)에 대해
dp[i][j] = dp[i][k] + dp[k+1][j] + 곱셈비용
곱셈비용: r[i] * c[k] * c[j]
'''

dp = [[0] * n for _ in range(n)]
for length in range(2, n+1):
    for i in range(n-length+1):
        j = i + length - 1
        dp[i][j] = 2**31
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1])

print(dp[0][-1])