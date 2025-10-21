import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5+5)

r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
max_cnt = 0
visited_set = set()

def dfs(x, y, cnt):
    global max_cnt
    max_cnt = max(max_cnt, cnt)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < c and 0 <= ny < r:
            if graph[ny][nx] not in visited_set:
                visited_set.add(graph[ny][nx])
                dfs(nx, ny, cnt+1)
                visited_set.remove(graph[ny][nx])

visited_set.add(graph[0][0])
dfs(0, 0, 1)
print(max_cnt)
