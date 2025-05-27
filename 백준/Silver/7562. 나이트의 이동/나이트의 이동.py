from collections import deque
import sys
input = sys.stdin.readline

def bfs(start_r, start_c, end_r, end_c):
    check = [[0] * l for _ in range(l)]
    q = deque([(start_r, start_c)])
    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [2, 1, -1, -2, -2, -1, 1, 2]
    while q:
        cr, cc = q.popleft()
        if cr == end_r and cc == end_c:
            return check[cr][cc]
        for i in range(8):
            nr, nc = cr + dy[i], cc + dx[i]
            if 0 <= nr < l and 0 <= nc < l and not check[nr][nc]:
                check[nr][nc] = check[cr][cc] + 1
                q.append((nr, nc))
            if nr == end_r and nc == end_c:
                return check[nr][nc]
    return -1

n = int(input())
for _ in range(n):
    l = int(input())
    start_r, start_c = map(int, input().split())
    end_r, end_c = map(int, input().split())
    print(bfs(start_r, start_c, end_r, end_c))
