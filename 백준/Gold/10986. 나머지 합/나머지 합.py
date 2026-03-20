import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

cntarr = [0] * m
cntarr[0] = 1

rem = 0
ans = 0

for num in arr:
    rem = (rem + num) % m
    ans += cntarr[rem]
    cntarr[rem] += 1

print(ans)