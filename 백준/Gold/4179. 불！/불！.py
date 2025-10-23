import sys
input = sys.stdin.readline
from collections import deque

r, c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]

fire = deque()
q = deque()

fire_time = [[-1] * c for _ in range(r)]
visited = [[-1] * c for _ in range(r)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(r):
    for j in range(c):
        if board[i][j] == 'F':
            fire.append((i, j))
            fire_time[i][j] = 0
        elif board[i][j] == 'J':
            q.append((i, j))
            visited[i][j] = 0

while fire:
    cr, cc = fire.popleft()
    for i in range(4):
        nr, nc = cr + dy[i], cc + dx[i]
        if 0 <= nr < r and 0 <= nc < c:
            if board[nr][nc] != '#' and fire_time[nr][nc] == -1:
                fire_time[nr][nc] = fire_time[cr][cc] + 1
                fire.append((nr, nc))

while q:
    cr, cc = q.popleft()
    if cr == 0 or cr == r-1 or cc == 0 or cc == c-1:
        print(visited[cr][cc] + 1)
        sys.exit()
    for i in range(4):
        nr, nc = cr + dy[i], cc + dx[i]
        if 0 <= nr < r and 0 <= nc < c:
            if board[nr][nc] != '#' and visited[nr][nc] == -1:
                if fire_time[nr][nc] == -1 or fire_time[nr][nc] > visited[cr][cc] + 1:
                    visited[nr][nc] = visited[cr][cc] + 1
                    q.append((nr, nc))

print("IMPOSSIBLE")