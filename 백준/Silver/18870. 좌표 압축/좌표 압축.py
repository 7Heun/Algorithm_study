import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
sorted_set = sorted((set(arr)))

result = {}
for i, v in enumerate(sorted_set):
    result[v] = i

for a in arr:
    print(result[a], end=' ')