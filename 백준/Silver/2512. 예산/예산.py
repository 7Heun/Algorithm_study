import sys
input = sys.stdin.readline

n = int(input())
requests = list(map(int, input().split()))
m = int(input())

left, right = 0, max(requests)
ans = 0
while left <= right:
    mid = (left+right) // 2
    total = sum(min(rq, mid) for rq in requests)
    if total > m:
        right = mid-1
    else:
        ans = mid
        left = mid+1
print(ans)