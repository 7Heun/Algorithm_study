from collections import defaultdict
import sys
sys.setrecursionlimit(2000)
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n + 1)

def dfs(v):
    visited[v] = True
    cnt = 1
    for n in graph[v]:
        if not visited[n]:
            cnt += dfs(n)
    return cnt

print(dfs(1) - 1)