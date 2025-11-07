import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5+5)

n, m = map(int, input().split())
edges = []

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()
parent = [i for i in range(n+1)]
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    aroot = find(a)
    broot = find(b)
    if aroot == broot:
        return False
    parent[broot] = aroot
    return True

total = 0
max_cost = 0
for c, a, b in edges:
    if union(a, b):
        total += c
        max_cost = c

print(total - max_cost)