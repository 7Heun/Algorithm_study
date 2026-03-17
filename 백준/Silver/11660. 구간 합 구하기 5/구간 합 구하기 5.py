import sys
input = sys.stdin.readline

'''
(2,2)~(3,4) -> dp[3][4] - dp[3][1] - dp[1][4] + dp[1][1]
(3,3)~(4,4) -> dp[4][4] - dp[4][2] - dp[2][4] + dp[2][2]
'''

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (n+1) for _ in range(n+1)]
dp[0][0] = board[0][0]
for i in range(1, n+1):
    dp[0][i] += dp[0][i-1] + board[0][i-1]
    dp[i][0] += dp[i-1][0] + board[i-1][0]
for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] += dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + board[i-1][j-1]


for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])
    