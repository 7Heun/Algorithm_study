import sys
input = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(10**5+5)

n = int(input())
m = int(input())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)
cnt = 0

def dfs(node):
    global cnt
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            cnt += 1
            dfs(neighbor)

dfs(1)
print(cnt)