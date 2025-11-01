import sys, heapq
input = sys.stdin.readline
from math import inf

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())

def dijkstra(start):
    hq = [(0, start)]
    dist = [inf] * (n+1)
    dist[start] = 0
    while hq:
        curr_c, curr = heapq.heappop(hq)
        if curr_c > dist[curr]: continue
        for nxt, nxt_c in graph[curr]:
            if curr_c + nxt_c < dist[nxt]:
                dist[nxt] = curr_c + nxt_c
                heapq.heappush(hq, (dist[nxt], nxt))
    return dist

first = dijkstra(1)
second = dijkstra(v1)
third = dijkstra(n)

# 1 -> v1 -> v2 -> n
ans1 = first[v1] + second[v2] + third[v2]
# 1 -> v2 -> v1 -> n
ans2 = first[v2] + second[v2] + third[v1]
print(-1 if ans1 == inf and ans2 == inf else min(ans1, ans2))