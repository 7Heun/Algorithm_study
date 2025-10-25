import sys
input = sys.stdin.readline
from collections import defaultdict

n, m = map(int, input().split())
graph = defaultdict(list)
visited = [False] * n

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

found = False
def dfs(node, depth):
    global found
    if found:
        return
    if depth == 4:
        found = True
        return
    visited[node] = True
    for nxt in graph[node]:
        if not visited[nxt]:
            dfs(nxt, depth+1)
    visited[node] = False

for i in range(n):
    dfs(i, 0)
    if found:
        print(1)
        break
else:
    print(0)