def solution(n):
    dp = [0] * max(4, n+1)
    dp[0], dp[1], dp[2] = 1, 1, 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[n]

n = int(input())
for _ in range(n):
    print(solution(int(input())))
