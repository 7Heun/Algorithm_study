import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5+5)

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    aroot = find(a)
    broot = find(b)
    if aroot != broot:
        parent[broot] = aroot

for _ in range(m):
    q, a, b = map(int, input().split())
    if q == 0:
        union(a, b)
    else:
        print("YES" if find(a) == find(b) else "NO")