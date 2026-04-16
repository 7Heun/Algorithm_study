import sys
input = sys.stdin.readline

'''
dfs
'ㅗ' 모양은 다르게 처리 (중심점 기준으로 방향 선택)
'''
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
max_val = max(map(max, board))

rows = [-1, 1, 0, 0]
cols = [0, 0, -1, 1]
ans = 0

def dfs(cr, cc, cnt, total):
    global ans
    # 남은 칸 수 고려해도 최댓값 안 되면 종료
    if total + max_val * (4 - cnt) <= ans: return

    # 4칸 완성
    if cnt == 4:
        ans = max(ans, total)
        return
    
    for d in range(4):
        nr, nc = cr + rows[d], cc + cols[d]
        if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
            # 'ㅗ' 모양 별도 처리
            if cnt == 2:
                visited[nr][nc] = True
                dfs(cr, cc, cnt + 1, total + board[nr][nc])
                visited[nr][nc] = False

            # 나머지 모양 처리
            visited[nr][nc] = True
            dfs(nr, nc, cnt + 1, total + board[nr][nc])
            visited[nr][nc] = False

for r in range(n):
    for c in range(m):
        visited[r][c] = True
        dfs(r, c, 1, board[r][c])
        visited[r][c] = False

print(ans)
