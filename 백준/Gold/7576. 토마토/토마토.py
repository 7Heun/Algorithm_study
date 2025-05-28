from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dq = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            dq.append((i, j, 0))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
max_day = 0

while dq:
    cy, cx, day = dq.popleft()
    for i in range(4):
        ny, nx = cy + dy[i], cx + dx[i]
        if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] == 0:
            arr[ny][nx] = 1
            dq.append((ny, nx, day+1))
            max_day = max(max_day, day+1)

for a in arr:
    if 0 in a:
        print(-1)
        break
else:
    print(max_day)