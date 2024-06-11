import sys
input = sys.stdin.readline
standard = [1, 1, 2, 2, 2, 8]
arr = list(map(int, input().split()))
for i in range(6):
    print(standard[i] - arr[i], end=' ')