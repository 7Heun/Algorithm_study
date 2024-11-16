from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    v[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if v[x][y] + maps[nx][ny] < v[nx][ny]:
                v[nx][ny] = v[x][y] + maps[nx][ny]
                q.append((nx, ny))

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    maps = [list(map(int, input())) for _ in range(n)]
    v = [[float('inf')] * n for _ in range(n)]
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    bfs(0, 0)
    ans = v[-1][-1]
    print(f"#{test_case} {ans}")