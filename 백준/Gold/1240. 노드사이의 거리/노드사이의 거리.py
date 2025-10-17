import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5+5)
from collections import defaultdict

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(n-1):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))

def dfs(now, target, dist, visited):
    if now == target:
        return dist
    visited[now] = True
    for n, d in graph[now]:
        if not visited[n]:
            res = dfs(n, target, dist+d, visited)
            if res: return res
    return 0

for _ in range(m):
    start, end = map(int, input().split())
    visited = [False] * (n+1)
    print(dfs(start, end, 0, visited))