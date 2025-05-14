import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0

def get_new_pos(r, c, d):
    nd = d
    for _ in range(4):
        nd = (nd + 3) % 4
        nr, nc = r + dx[nd], c + dy[nd]
        if 0 <= nr < N and 0 <= nc < M and not arr[nr][nc]:
            return nr, nc, nd
    return -1, -1, -1      
    
while True:
    if not arr[r][c]:
        arr[r][c] = 2
        cnt += 1
    nr, nc, nd = get_new_pos(r, c, d)
    if not (nr == -1 and nc == -1 and nd == -1):
        r, c, d = nr, nc, nd
        continue
    nd = (d + 2) % 4
    nr, nc = r + dx[nd], c + dy[nd]
    if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != 1:
        r, c = nr, nc
    else:
        break

print(cnt)