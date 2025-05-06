import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def bfs(x, y):
    queue = deque([(x, y)])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    area = 1
    visited[y][x] = True
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if not (0 <= nx < m and 0 <= ny < n): continue
            if not visited[ny][nx] and graph[ny][nx]:
                visited[ny][nx] = True
                queue.append((nx, ny))
                area += 1
    return area
        
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
visited = [[False] * m for _ in range(n)]
ans = []
for y in range(n):
    for x in range(m):
        if not visited[y][x] and graph[y][x]:
            ans.append(bfs(x, y))
ans.sort(reverse=True)

print(len(ans))
print(ans[0] if ans else 0)