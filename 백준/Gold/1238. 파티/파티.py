import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    dist = [float('inf')] * (N + 1)
    dist[start] = 0
    hq = [(0, start)]   # 다음 방문 노드

    while hq:
        cost, node = heapq.heappop(hq)
        if cost > dist[node]:   # 이미 더 짧은 경로 있으면 무시
            continue
        for next_node, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heapq.heappush(hq, (new_cost, next_node))
    return dist

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))

max_dist = 0
back_dist = dijkstra(X) # X -> i

for i in range(1, N+1):
    go_dist = dijkstra(i)
    max_dist = max(max_dist, go_dist[X] + back_dist[i])

print(max_dist)
    