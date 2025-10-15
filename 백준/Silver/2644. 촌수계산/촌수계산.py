import sys
input = sys.stdin.readline
from collections import defaultdict, deque

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = defaultdict(list)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(start, end):
    dq = deque([start])
    distance = [0] * (n+1)
    while dq:
        node = dq.popleft()
        for neighbor in graph[node]:
            if not distance[neighbor]:
                distance[neighbor] = distance[node] + 1
                if neighbor == end:
                    return distance[neighbor]
                dq.append(neighbor)
    return -1

print(bfs(a, b))