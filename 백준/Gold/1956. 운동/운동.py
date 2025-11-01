import sys
input = sys.stdin.readline
from math import inf

v, e = map(int, input().split())
dist = [[inf] * (v+1) for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    dist[a][b] = c

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

ans = inf
for i in range(1, v+1):
    ans = min(ans, dist[i][i])
print(ans if ans != inf else -1)