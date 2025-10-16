import sys
input = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(10**5+5)

def dfs(start):
    for child in tree[start]:
        cnt[child] += cnt[start]
        dfs(child)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
tree = defaultdict(list)

for i in range(1, n+1):
    if arr[i-1] != -1:
        tree[arr[i-1]].append(i)

cnt = [0] * (n+1)
for _ in range(m):
    i, w = map(int, input().split())
    cnt[i] += w

dfs(1)
print(*cnt[1:])
