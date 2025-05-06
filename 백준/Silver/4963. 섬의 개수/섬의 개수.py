import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y):
    visited[y][x] = True
    dx = [-1, 1, 0, 0, -1, 1, -1, 1]
    dy = [0, 0, -1, 1, -1, -1, 1, 1]
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if not (0 <= nx < w and 0 <= ny < h): continue
        if not visited[ny][nx] and graph[ny][nx]:
            dfs(nx, ny)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0: break
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    visited = [[False] * w for _ in range(h)]
    ans = 0
    for i in range(w):
        for j in range(h):
            if not visited[j][i] and graph[j][i]:
                dfs(i, j)
                ans += 1
    print(ans)
