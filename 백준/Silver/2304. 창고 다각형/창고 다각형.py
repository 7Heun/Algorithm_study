import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()
max_i = arr.index(max(arr, key = lambda x: x[1]))

left = 0
right = N-1
total = 0
for i in range(max_i):
    if arr[i][1] > arr[left][1]:
        total += arr[left][1] * (arr[i][0] - arr[left][0])
        left = i
total += arr[left][1] * (arr[max_i][0] - arr[left][0])
for i in range(N-1, max_i, -1):
    if arr[i][1] > arr[right][1]:
        total += arr[right][1] * (arr[right][0] - arr[i][0])
        right = i
total += arr[right][1] * (arr[right][0] - arr[max_i][0])
print(total + arr[max_i][1])