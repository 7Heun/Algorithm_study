import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
max_day = 0

def bfs():
    q = deque()
    max_day = 0

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                q.append((i, j, 0))
    while q:
        r, c, day = q.popleft()
        for i in range(4):
            nr, nc = r + dy[i], c + dx[i]
            if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == 0:
                board[nr][nc] = 1
                q.append((nr, nc, day+1))
                max_day = max(max_day, day+1)
    return max_day

ans = bfs()

for row in board:
    if 0 in row:
        print(-1)
        break
else:
    print(ans)