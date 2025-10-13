import sys
input = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(10**5+5)

n = int(input())
graph = defaultdict(list)
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

parents = [0] * (n+1)
def dfs(node, parent):
    parents[node] = parent
    for neighbor in graph[node]:
        if not parents[neighbor]:
            dfs(neighbor, node)

dfs(1, 0)
for i in range(2, n+1):
    print(parents[i])