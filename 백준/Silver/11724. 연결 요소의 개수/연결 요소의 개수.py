from collections import defaultdict
import sys
sys.setrecursionlimit(2000)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = defaultdict(list)
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    visited[v] = True
    for n in graph[v]:
        if not visited[n]:
            dfs(n)

ans = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        ans += 1

print(ans)