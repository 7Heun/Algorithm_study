import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y):
    visited[y][x] = True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not (0 <= nx < N and 0 <= ny < N): continue
        if not visited[ny][nx] and graph[ny][nx]:
            cnt += dfs(nx, ny)
    return cnt

N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
ans = []
for y in range(N):
    for x in range(N):
        if not visited[y][x] and graph[y][x]:
            ans.append(dfs(x, y))
ans.sort()
print(len(ans))
print(*ans, sep='\n')