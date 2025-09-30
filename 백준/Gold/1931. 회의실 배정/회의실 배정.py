import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
sorted_arr = sorted(arr, key=lambda x: (x[1], x[0]))

now = 0
cnt = 0
for s, e in sorted_arr:
    if s >= now:
        now = e
        cnt += 1
print(cnt)