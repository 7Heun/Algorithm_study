import sys
input = sys.stdin.readline

'''
B 부분 LIS
dp[i]: i번째 조합을 마지막이라고 할 때 연결할 수 있는 전깃줄의 최대 개수
'''
n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort()

dp = [1] * n
for i in range(n):
    for j in range(i):
        if arr[j][1] < arr[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))