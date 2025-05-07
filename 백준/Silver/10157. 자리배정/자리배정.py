import sys
input = sys.stdin.readline
c, r = map(int, input().split())
k = int(input())
if k > c * r:
    print(0)
    exit()

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
visited = [[False] * c for _ in range(r)]
x, y = 0, 0
visited[y][x] = True
cnt = 1
i = 0
while cnt < k:
    nx, ny = x + dx[i % 4], y + dy[i % 4]
    if not (0 <= nx < c and 0 <= ny < r):
        i += 1
        continue
    if visited[ny][nx]:
        i += 1
        continue
    visited[ny][nx] = True
    x, y = nx, ny
    cnt += 1
print(x+1, y+1)
