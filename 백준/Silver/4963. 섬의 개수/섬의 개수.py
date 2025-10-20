import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 0, -1, 1, -1, 1, -1, 1]
dy = [1, -1, 0, 0, 1, 1, -1, -1]
def bfs(i, j):
    q = deque([(i, j)])
    visited[i][j] = 1
    while q:
        r, c = q.popleft()
        for d in range(8):
            nr, nc = r + dy[d], c + dx[d]
            if 0 <= nr < h and 0 <= nc < w:
                if graph[nr][nc] and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    q.append((nr, nc))

while True:
    w, h = map(int, input().split())
    if not w and not h: break
    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    print(cnt)