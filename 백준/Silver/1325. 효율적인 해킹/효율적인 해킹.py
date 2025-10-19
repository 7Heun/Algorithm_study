import sys
input = sys.stdin.readline
from collections import defaultdict, deque

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(start):
    visited = [0] * (n+1)
    visited[start] = 1
    q = deque([start])
    cnt = 1

    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = 1
                q.append(nxt)
                cnt += 1
    return cnt

res = [0] * (n+1)
max_cnt = 0
for i in range(1, n+1):
    res[i] = bfs(i)
    max_cnt = max(max_cnt, res[i])

for i in range(1, n+1):
    if res[i] == max_cnt:
        print(i, end=' ')