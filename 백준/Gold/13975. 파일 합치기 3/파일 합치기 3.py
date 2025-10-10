import sys, heapq
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    files = list(map(int, input().split()))
    heapq.heapify(files)

    total = 0
    while len(files) > 1:
        add = heapq.heappop(files) + heapq.heappop(files)
        total += add
        heapq.heappush(files, add)
    print(total)