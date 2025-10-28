import sys, heapq
input = sys.stdin.readline
from collections import defaultdict

V, E = map(int, input().split())
K = int(input())
graph = defaultdict(list)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start):
    hq = []
    distance = [float('INF')] * (V+1)
    heapq.heappush(hq, (0, start))
    distance[start] = 0
    while hq:
        dist, now = heapq.heappop(hq)
        if distance[now] < dist:
            continue
        for nxt, w in graph[now]:
            if distance[now] + w < distance[nxt]:
                distance[nxt] = distance[now] + w
                heapq.heappush(hq, (distance[nxt], nxt))
        
    return distance

distance = dijkstra(K)
for i in range(1, V+1):
    print(distance[i] if distance[i] < float('INF') else 'INF')