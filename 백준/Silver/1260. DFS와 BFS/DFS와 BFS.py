import sys
input = sys.stdin.readline
from collections import defaultdict, deque
sys.setrecursionlimit(10**5+5)

n, m, v = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(g, start):
    visited = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(sorted(g[node], reverse=True))
    return visited

def bfs(g, start):
    visited = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(sorted(g[node]))
    return visited

print(*dfs(graph, v))
print(*bfs(graph, v))