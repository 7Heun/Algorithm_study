import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
brr = list(map(int, input().split()))

cntarr = defaultdict(int)
for a in arr:
    cntarr[a] += 1

for b in brr:
    print(cntarr[b], end=' ')