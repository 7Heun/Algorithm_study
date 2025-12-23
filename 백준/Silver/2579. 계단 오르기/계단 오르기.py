import sys
input = sys.stdin.readline

n = int(input())
scores = [int(input()) for _ in range(n)]

'''
i-3, i-2, i-1, i
1. i-2 밟, i-1 안밟, i 도착 (i-2 -> i)
2. i-3 밟, i-2 안밟, i-1 밟, i 도착 (i-3 -> i-1 -> i)
'''
if n == 1:
    print(scores[0])
    sys.exit()
if n == 2:
    print(scores[0] + scores[1])
    sys.exit()

dp = [0] * n
dp[0] = scores[0]
dp[1] = scores[0] + scores[1]
dp[2] = max(scores[0] + scores[2], scores[1] + scores[2])

for i in range(3, n):
    dp[i] = max(dp[i-2] + scores[i], dp[i-3] + scores[i-1] + scores[i])

print(dp[-1])