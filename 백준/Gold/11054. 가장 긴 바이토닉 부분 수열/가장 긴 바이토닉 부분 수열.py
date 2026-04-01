import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

def set_dp(arr):
    dp = [1] * n
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] < arr[j]:
                dp[j] = max(dp[j], dp[i] + 1)
    return dp

dp_inc = set_dp(arr)
dp_dec = set_dp(arr[-1::-1])
dp_dec.reverse()

ans = 0
for i in range(n):
    ans = max(ans, dp_inc[i] + dp_dec[i] - 1)
print(ans)
