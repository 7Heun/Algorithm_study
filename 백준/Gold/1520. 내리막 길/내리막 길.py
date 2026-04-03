import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]

'''
dp[i][j]: (i, j)에서 (m, n)까지 가는 경우의 수
인접한 칸 중 가능한 칸의 경우의 수를 더하기
'''
dp = [[-1] * n for _ in range(m)]
rows = [0, 0, -1, 1]
cols = [1, -1, 0, 0]

def dfs(x, y):
    if x == m-1 and y == n-1: return 1
    if dp[x][y] != -1: return dp[x][y]
    dp[x][y] = 0
    for i in range(4):
        nx, ny = x + rows[i], y + cols[i]
        if not (0 <= nx < m and 0 <= ny < n): continue
        if board[nx][ny] < board[x][y]:
            dp[x][y] += dfs(nx, ny)
    return dp[x][y]

print(dfs(0, 0))