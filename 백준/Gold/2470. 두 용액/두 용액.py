import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
min_sum = 2000000000
ans = (0, 0)
left, right = 0, N-1

while left < right:
    s = arr[left] + arr[right]
    if abs(s) < min_sum:
        ans = (arr[left], arr[right])
        min_sum = abs(s)
    if s < 0:
        left += 1
    elif s > 0:
        right -= 1
    else:
        break
print(*ans)