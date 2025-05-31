import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

total = 0
left = 0
min_len = float('inf')

for right in range(N):
    total += arr[right]
    while total >= S:
        min_len = min(min_len, right - left + 1)
        total -= arr[left]
        left += 1

print(min_len if min_len != float('inf') else 0)