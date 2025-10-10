import sys, heapq
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
heapq.heapify(arr)
total = 0

while len(arr) >= 2:
    add = heapq.heappop(arr) + heapq.heappop(arr)
    heapq.heappush(arr, add)
    total += add

print(total)