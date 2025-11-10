import sys
input = sys.stdin.readline

n, k = map(int, input().split())
item = []
for _ in range(n):
    w, v = map(int, input().split())
    item.append((w, v))

dp = [[0] * (k+1) for _ in range(n+1)]
for i in range(1, n+1):
    w, v = item[i-1]
    for j in range(k+1):
        # 현재 물건 안 넣는 경우
        dp[i][j] = dp[i-1][j]
        # 넣을 수 있는 경우 넣어보기
        if w <= j:
            dp[i][j] = max(dp[i][j], dp[i-1][j-w] + v)

print(dp[n][k])