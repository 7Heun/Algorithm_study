import sys, heapq
input = sys.stdin.readline
from math import inf

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
start, end = map(int, input().split())

def dijkstra(start):
    dist = [inf] * (n+1)
    dist[start] = 0
    hq = [(0, start)]
    while hq:
        curr_cost, curr = heapq.heappop(hq)
        if curr_cost > dist[curr]: continue
        for nxt, nxt_cost in graph[curr]:
            if curr_cost + nxt_cost < dist[nxt]:
                dist[nxt] = curr_cost + nxt_cost
                heapq.heappush(hq, (dist[nxt], nxt))
    return dist

dist = dijkstra(start)
print(dist[end])
