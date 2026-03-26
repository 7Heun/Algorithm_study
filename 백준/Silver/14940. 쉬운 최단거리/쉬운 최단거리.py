import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]
rows = [0, 0, 1, -1]
cols = [1, -1, 0, 0]

q = deque()

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            dist[i][j] = 0
        elif board[i][j] == 2:
            dist[i][j] = 0
            q.append((i, j))

while q:
    cr, cc = q.popleft()
    for d in range(4):
        nr, nc = cr + rows[d], cc + cols[d]
        if not (0 <= nr < n and 0 <= nc < m): continue
        if board[nr][nc] == 1 and dist[nr][nc] < 0:
            dist[nr][nc] = dist[cr][cc] + 1
            q.append((nr, nc))

for d in dist:
    print(*d)