import sys
input = sys.stdin.readline

n, new, p = map(int, input().split())
scores = list(map(int, input().split())) if n else []

e = sum(1 for s in scores if s >= new)
if e >= p: print(-1)
else:
    t = sum(1 for s in scores if s > new)
    print(t+1)