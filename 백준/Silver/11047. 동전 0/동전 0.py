import sys
input = sys.stdin.readline
n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.sort(reverse=True)
cnt = 0
while k:
    cnt += k // a[0]
    k %= a[0]
    a.pop(0)
print(cnt)