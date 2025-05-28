from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
water = deque()
hedgehog = deque()
for i in range(R):
    for j in range(C):
        if board[i][j] == 'S':
            hedgehog.append((i, j, 0))
        elif board[i][j] == '*':
            water.append((i, j))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[False] * C for _ in range(R)]

while hedgehog:
    for _ in range(len(water)):
        r, c = water.popleft()
        for i in range(4):
            nr, nc = r + dy[i], c + dx[i]
            if 0 <= nr < R and 0 <= nc < C and board[nr][nc] == '.':
                board[nr][nc] = '*'
                water.append((nr, nc))

    for _ in range(len(hedgehog)):
        hr, hc, cnt = hedgehog.popleft()
        for i in range(4):
            nhr, nhc = hr + dy[i], hc + dx[i]
            if 0 <= nhr < R and 0 <= nhc < C:
                if board[nhr][nhc] == 'D':
                    print(cnt+1)
                    exit()
                if board[nhr][nhc] == '.' and not visited[nhr][nhc]:
                    visited[nhr][nhc] = True
                    hedgehog.append((nhr, nhc, cnt+1))
        
print('KAKTUS')