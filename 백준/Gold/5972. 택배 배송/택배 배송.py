import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    dist = [float('inf')] * (N + 1)
    hq = [(0, start)]
    while hq:
        cost, node = heapq.heappop(hq)
        if cost > dist[node]:
            continue
        for next_node, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heapq.heappush(hq, (new_cost, next_node))
    return dist

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dist = dijkstra(1)
print(dist[N])