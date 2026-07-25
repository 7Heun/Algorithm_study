'''
우,하로만 움직여야 함
최단경로의 개수
물이면 못 감
1-based
dp[n][m]
'''
from collections import deque

def solution(m, n, puddles):
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            # 시작점이면 패스
            if i == 1 and j == 1: continue
            # 물웅덩이면 패스
            if [j, i] in puddles: 
                dp[i][j] = 0
                continue
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
    
    return dp[n][m]
