import sys, heapq
input = sys.stdin.readline

n = int(input())
lectures = [tuple(map(int, input().split())) for _ in range(n)]
lectures.sort()

hq = []
for start, end in lectures:
    if hq and hq[0] <= start:
        heapq.heappop(hq)
    heapq.heappush(hq, end)

print(len(hq))