import sys
input = sys.stdin.readline

'''
dp[n][k]: 1~k를 사용해 n을 만드는 경우의 수
1. k를 사용하지 않고 n을 만드는 경우 -> dp[n][k-1]
2. k를 적어도 한 번 사용해서 n을 만드는 경우 -> dp[n-k][k]
d[n][k] = dp[n][k-1] + dp[n-k][k]
'''

def find_case():
    MAX = 10001
    dp = [[0] * 4 for _ in range(MAX)]
    # 초기값
    for k in range(1, 4):
        dp[0][k] = 1
    for i in range(1, MAX):
        for j in range(1, 4):
            if i - j >= 0:
                dp[i][j] = dp[i][j-1] + dp[i-j][j]
            else:
                dp[i][j] = dp[i][j-1]
    return dp

T = int(input())

for _ in range(T):
    n = int(input())
    dp = find_case()
    print(dp[n][3])