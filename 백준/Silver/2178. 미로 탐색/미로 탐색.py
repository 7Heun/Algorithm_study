import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    queue = deque([(x, y)])
    visited[y][x] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if not (0 <= nx < M and 0 <= ny < N): continue
            if not visited[ny][nx] and graph[ny][nx]:
                visited[ny][nx] = visited[cy][cx] + 1
                queue.append((nx, ny))

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().strip())))
visited = [[0] * M for _ in range(N)]
bfs(0, 0)
print(visited[-1][-1])
