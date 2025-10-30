import sys, heapq
input = sys.stdin.readline
from math import inf

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
reversed_graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))
    reversed_graph[e].append((s, t))

def dijkstra(start, graph):
    dist = [inf] * (n+1)
    dist[start] = 0
    hq = [(0, start)]

    while hq:
        now_t, now = heapq.heappop(hq)
        if now_t > dist[now]: continue
        for nxt, nxt_t in graph[now]:
            if now_t + nxt_t < dist[nxt]:
                dist[nxt] = now_t + nxt_t
                heapq.heappush(hq, (dist[nxt], nxt))
    return dist

go = dijkstra(x, reversed_graph)
back = dijkstra(x, graph)

ans = max(go[i] + back[i] for i in range(1, n+1))
print(ans)