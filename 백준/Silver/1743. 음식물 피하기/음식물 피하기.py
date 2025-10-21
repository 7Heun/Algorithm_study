import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def bfs(i, j):
    q = deque([(i, j)])
    visited[i][j] = 1
    cnt = 1
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr, nc = r + dy[d], c + dx[d]
            if 0 <= nr < n and 0 <= nc < m:
                if graph[nr][nc] and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    q.append((nr, nc))
                    cnt += 1
    return cnt

n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 1
ans = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] and not visited[i][j]:
            cnt = bfs(i, j)
            ans = max(ans, cnt)
            
print(ans)
