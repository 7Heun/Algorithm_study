import sys
input = sys.stdin.readline
from collections import defaultdict, deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
max_height = max(map(max, board))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 연결된 부분 체크 bfs
def bfs(r, c, h):
    dq = deque([(r, c)])
    visited[r][c] = True
    while dq:
        cr, cc = dq.popleft()
        for d in range(4):
            nr, nc = cr + dy[d], cc + dx[d]
            if 0 <= nr < n and 0 <= nc < n:
                if not visited[nr][nc] and board[nr][nc] > h:
                    visited[nr][nc] = True
                    dq.append((nr, nc))

ans = 0
for height in range(max_height+1):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and board[i][j] > height:
                bfs(i, j, height)
                cnt += 1
    ans = max(ans, cnt)

print(ans)