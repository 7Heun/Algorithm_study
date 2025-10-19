import sys
input = sys.stdin.readline
from collections import defaultdict, deque

# 가장 긴 최소경로 찾기
n = int(input())
graph = defaultdict(list)
for _ in range(n-1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

def bfs(start):
    q = deque([start])
    distance = [-1] * (n+1)
    distance[start] = 0
    while q:
        now = q.popleft()
        for nxt_n, nxt_w in graph[now]:
            if distance[nxt_n] < 0:
                distance[nxt_n] = distance[now] + nxt_w
                q.append(nxt_n)
    max_dist = max(distance)
    return distance.index(max_dist), max_dist

# 한쪽 끝 찾기
end, _ = bfs(1)
# end -> 가장 먼 노드 거리
_, ans = bfs(end)
print(ans)