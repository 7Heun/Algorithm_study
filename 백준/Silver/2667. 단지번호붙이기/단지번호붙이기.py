import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

n = int(input())
board = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

def bfs(r, c):
    q = deque([(r, c)])
    cnt = 1
    while q:
        cr, cc = q.popleft()
        for d in range(4):
            nr, nc = cr + dy[d], cc + dx[d]
            if 0 <= nr < n and 0 <= nc < n:
                if board[nr][nc] and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    cnt += 1
                    q.append((nr, nc))
    return cnt

total = []
for i in range(n):
    for j in range(n):
        if board[i][j] and not visited[i][j]:
            visited[i][j] = 1
            total.append(bfs(i, j))
print(len(total))
total.sort()
for t in total:
    print(t)