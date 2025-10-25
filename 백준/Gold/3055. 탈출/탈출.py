import sys
input = sys.stdin.readline
from collections import deque

r, c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]

water = deque()
q = deque()
water_time = [[-1] * c for _ in range(r)]
visited = [[-1] * c for _ in range(r)]

for i in range(r):
    for j in range(c):
        if board[i][j] == '*':
            water.append((i, j))
            water_time[i][j] = 0
        elif board[i][j] == 'S':
            q.append((i, j))
            visited[i][j] = 0

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

while water:
    y, x = water.popleft()
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < c and 0 <= ny < r:
            if board[ny][nx] not in ('X', 'D') and water_time[ny][nx] == -1:
                water_time[ny][nx] = water_time[y][x] + 1
                water.append((ny, nx))

while q:
    y, x = q.popleft()
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < c and 0 <= ny < r:
            if board[ny][nx] == 'D':
                print(visited[y][x]+1)
                sys.exit()
            if board[ny][nx] == '.' and visited[ny][nx] == -1:
                if water_time[ny][nx] == -1 or water_time[ny][nx] > visited[y][x] + 1:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny, nx))
print("KAKTUS")