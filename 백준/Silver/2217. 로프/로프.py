import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)

max_w = 0
for i in range(n):
    max_w = max(max_w, arr[i] * (i+1))

print(max_w)