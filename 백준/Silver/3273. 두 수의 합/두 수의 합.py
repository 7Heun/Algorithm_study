import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())
arr.sort()
ans = 0
left, right = 0, n-1
while left < right:
    s = arr[left] + arr[right]
    if s == x:
        ans += 1
        left += 1
        right -=1
    elif s > x:
        right -= 1
    else:
        left += 1
print(ans)