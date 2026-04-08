import sys
input = sys.stdin.readline

'''
dp[i][j]: i부터 j까지 합치는 최소 비용
s에서 자른다고 하면
dp[i][j] = min(dp[i][s] + dp[s+1][j] + sum(i~j))
'''

t = int(input())
for _ in range(t):
    k = int(input())
    files = list(map(int, input().split()))
    dp = [[float('inf')] * (k) for _ in range(k)]
    add = [0] * (k+1)
    for i in range(1, k+1):
        add[i] = add[i-1] + files[i-1]

    for i in range(k):
        dp[i][i] = 0
    
    # 구간 길이 기준
    for length in range(2, k+1):
        for i in range(k - length + 1):
            j = i + length - 1
            for s in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][s] + dp[s+1][j] + add[j+1] - add[i])

    print(dp[0][k-1])