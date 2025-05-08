import sys
input = sys.stdin.readline
N, K = map(int, input().split())
arr = list(map(int, input().split()))
total = sum(arr[:K])
max_sum = total
for i in range(K, N):
    total = total - arr[i-K] + arr[i]
    if total > max_sum: max_sum = total
print(max_sum)