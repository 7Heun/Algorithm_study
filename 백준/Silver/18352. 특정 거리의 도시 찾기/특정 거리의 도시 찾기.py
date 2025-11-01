import sys
input = sys.stdin.readline
from collections import deque, defaultdict

n, m, k, x = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(start):
    q = deque([start])
    dist = [-1] * (n+1)
    dist[start] = 0
    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if dist[nxt] < 0:
                dist[nxt] = dist[now] + 1
                q.append(nxt)
    return dist

dist = bfs(x)
ans = []
for i in range(1, n+1):
    if dist[i] == k:
        ans.append(i)
if ans:
    ans.sort()
    for a in ans:
        print(a)
else:
    print(-1)