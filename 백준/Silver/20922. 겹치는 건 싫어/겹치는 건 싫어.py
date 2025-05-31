from collections import defaultdict
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

count = defaultdict(int)
left = right = max_len = 0

while right < N:
    count[arr[right]] += 1
    while count[arr[right]] > K:
        count[arr[left]] -= 1
        left += 1
    max_len = max(max_len, right - left + 1)
    right += 1

print(max_len)