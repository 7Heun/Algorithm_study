import sys, heapq
input = sys.stdin.readline

n, k = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]

jewels.sort()
bags.sort()

hq = []
i = 0
ans = 0

for bag in bags:
    while i < n and jewels[i][0] <= bag:
        heapq.heappush(hq, -jewels[i][1])
        i += 1
    if hq:
        ans += -heapq.heappop(hq)
print(ans)