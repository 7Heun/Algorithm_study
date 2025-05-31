from collections import defaultdict
import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(N)]

count = defaultdict(int)
unique = 0

for i in range(k):
    if count[arr[i]] == 0:
        unique += 1
    count[arr[i]] += 1

ans = unique + (0 if count[c] else 1)

for i in range(1, N):
    left = arr[i-1]
    count[left] -= 1
    if count[left] == 0:
        unique -= 1
    
    right = arr[(i+k-1) % N]
    if count[right] == 0:
        unique += 1
    count[right] += 1

    total = unique + (0 if count[c] else 1)
    ans = max(ans, total)

print(ans)