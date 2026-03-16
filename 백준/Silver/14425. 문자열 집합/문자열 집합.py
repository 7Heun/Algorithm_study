import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = set(input().strip() for _ in range(n))

ans = 0

for _ in range(m):
    q = input().strip()
    if q in s:
        ans += 1
print(ans)