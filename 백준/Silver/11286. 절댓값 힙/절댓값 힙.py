import sys, heapq
input = sys.stdin.readline

n = int(input())
hq = []

for _ in range(n):
    x = int(input())
    if x:
        heapq.heappush(hq, (abs(x), x))
    else:
        print(heapq.heappop(hq)[1] if hq else 0)
