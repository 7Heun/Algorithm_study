import sys
input = sys.stdin.readline 

n, k, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
cnt = 0
idx = 0
direction = 1
while arr:
    add = k-1 if direction == 1 else k
    idx = (idx + direction * add) % len(arr)
    print(arr.pop(idx))
    cnt += 1
    if cnt == m:
        direction *= -1
        cnt = 0