import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
def bfs(r, c):
    q = deque([(r, c)])
    visited[r][c] = 1
    while q:
        cr, cc = q.popleft()
        if graph[cr][cc] == '-' and cc+1 < m:
            nr, nc = cr, cc+1
        elif graph[cr][cc] == '|' and cr+1 < n:
            nr, nc = cr+1, cc
        else:
            continue
        if not visited[nr][nc] and graph[cr][cc] == graph[nr][nc]:
            visited[nr][nc] = 1
            q.append((nr, nc))

ans = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            bfs(i, j)
            ans += 1
print(ans)