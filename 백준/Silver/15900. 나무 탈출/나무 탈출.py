import sys
input = sys.stdin.readline
from collections import defaultdict

def dfs(node):
    stack = [(node, 0)]
    visited = [False] * (n+1)
    visited[node] = True
    total = 0
    while stack:
        now, depth = stack.pop()
        is_leaf = True
        for neighbor in graph[now]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append((neighbor, depth+1))
                is_leaf = False
        if is_leaf:
            total += depth
    return total

graph = defaultdict(list)
n = int(input())
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

total = dfs(1)
print("Yes" if total % 2 else "No")