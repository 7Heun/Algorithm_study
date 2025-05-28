from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

def bfs(board, pos, fire):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False] * w for _ in range(h)]
    while pos:
        for _ in range(len(fire)):
            r, c = fire.popleft()
            for i in range(4):
                nr, nc = r + dy[i], c + dx[i]
                if 0 <= nr < h and 0 <= nc < w and board[nr][nc] == '.':
                    board[nr][nc] = '*'
                    fire.append((nr, nc))
        for _ in range(len(pos)):
            r, c, cnt = pos.popleft()
            for i in range(4):
                nr, nc = r + dy[i], c + dx[i]
                if not (0 <= nr < h and 0 <= nc < w):
                    return cnt + 1
                if board[nr][nc] == '.' and not visited[nr][nc]:
                    visited[nr][nc] = True
                    pos.append((nr, nc, cnt+1))
    return "IMPOSSIBLE"

for _ in range(t):
    w, h = map(int, input().split())
    board = [list(input()) for _ in range(h)]
    pos = deque()
    fire = deque()
    for i in range(h):
        for j in range(w):
            if board[i][j] == '@':
                pos.append((i, j, 0))
            if board[i][j] == '*':
                fire.append((i, j))
    print(bfs(board, pos, fire))
