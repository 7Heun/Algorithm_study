from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
blanks = []
viruses = deque()
for i in range(N):
    for j in range(M):
        if not arr[i][j]:
            blanks.append((i, j))
        elif arr[i][j] == 2:
            viruses.append((i, j))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(board):
    copied_viruses = deque(viruses)
    while copied_viruses:
        r, c = copied_viruses.popleft()
        for i in range(4):
            nc, nr = c + dx[i], r + dy[i]
            if 0 <= nr < N and 0 <= nc < M and not board[nr][nc]:
                board[nr][nc] = 2
                copied_viruses.append((nr, nc))
    return board

ans = 0
for walls in combinations(blanks, 3):
    board = [row[:] for row in arr]
    for r, c in walls:
        board[r][c] = 1
    
    board = bfs(board)

    safe = sum(b.count(0) for b in board)
    ans = max(ans, safe)

print(ans)