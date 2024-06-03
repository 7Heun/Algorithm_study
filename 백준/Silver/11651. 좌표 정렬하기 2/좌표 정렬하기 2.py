import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
points.sort(key = lambda x: (x[1], x[0]))

for x, y in points:
    print(f"{x} {y}\n")