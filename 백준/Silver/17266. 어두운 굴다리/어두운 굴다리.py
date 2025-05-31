import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
lamps = list(map(int, input().split()))

left, right = 0, N
min_h = N
while left <= right:
    mid = (left + right) // 2
    last = 0
    success = True
    for lamp in lamps:
        if lamp - mid > last:
            success = False
            break
        last = lamp + mid
    if success and last >= N:
        min_h = mid
        right = mid - 1
    else:
        left = mid + 1
print(min_h)
