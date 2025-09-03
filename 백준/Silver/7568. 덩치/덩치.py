import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = []
for i in range(n):
    cnt = 1
    for j in range(n):
        if i == j: continue
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            cnt += 1
    ans.append(cnt)
print(*ans)