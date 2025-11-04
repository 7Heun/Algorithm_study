import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5+5)

v, e = map(int, input().split())
edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()

parent = [i for i in range(v+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    aroot = find(a)
    broot = find(b)
    if aroot == broot: return False
    parent[broot] = aroot
    return True

total = 0
for c, a, b in edges:
    if union(a, b):
        total += c

print(total)