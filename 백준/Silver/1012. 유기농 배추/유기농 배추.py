import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
T = int(input())

def dfs(x, y):
    visited[y][x] = True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not (0 <= nx < M and 0 <= ny < N): continue
        if not visited[ny][nx] and graph[ny][nx]:
            dfs(nx, ny)
    
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
            if graph[n][m] == 1 and not visited[n][m]:
                dfs(m, n)
                ans += 1
    print(ans)