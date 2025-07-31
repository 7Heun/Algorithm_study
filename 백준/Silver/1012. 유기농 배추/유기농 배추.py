import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def dfs(x, y):
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        if visited[cy][cx]: continue
        visited[cy][cx] = True
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if not (0 <= nx < M and 0 <= ny < N): continue
            if not visited[ny][nx] and graph[ny][nx]:
                stack.append((nx, ny))

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    ans = 0
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
    for n in range(N):
        for m in range(M):
            if not visited[n][m] and graph[n][m]:
                dfs(m, n)
                ans += 1
    print(ans)
    