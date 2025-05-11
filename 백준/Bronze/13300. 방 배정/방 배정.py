import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [[0] * 2 for _ in range(6)]
ans = 0

for _ in range(N):
    S, Y = map(int, input().split())
    arr[Y-1][S] += 1

for a in arr:
    for i in range(2):
        ans += (a[i] + K - 1) // K

print(ans)