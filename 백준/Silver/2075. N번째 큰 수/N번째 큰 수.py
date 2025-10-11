import sys, heapq
input = sys.stdin.readline

n = int(input())
hq = []

for _ in range(n):
    for now in map(int, input().split()):
        if len(hq) < n:
            heapq.heappush(hq, now)
        elif now > hq[0]:
            heapq.heappushpop(hq, now)
print(hq[0])