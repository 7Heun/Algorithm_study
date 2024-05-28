import sys
input = sys.stdin.readline
N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
points.sort()
for x, y in points:
    print(x, y)