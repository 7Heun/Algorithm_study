from collections import deque
import sys
input = sys.stdin.readline

'''
bfs
같은 색이 4개 이상 붙어있는 부분 찾기 -> 연쇄 카운트
터지고 남은 뿌요들 아래로 내리기
'''
board = [list(input().strip()) for _ in range(12)]

rows = [0, 1, 0, -1]
cols = [1, 0, -1, 0]

def bfs(r, c, color):
    dq = deque([(r, c)])
    visited[r][c] = True
    group = [(r, c)]

    while dq:
        cr, cc = dq.popleft()
        for d in range(4):
            nr, nc = cr + rows[d], cc + cols[d]
            if not (0 <= nr < 12 and 0 <= nc < 6): continue
            if visited[nr][nc]: continue
            
            if board[nr][nc] == color:
                visited[nr][nc] = True
                dq.append((nr, nc))
                group.append((nr, nc))

    if len(group) >= 4:
        return group
    return []

def down():
    for c in range(6):
        # 아래에서부터 뿌요 그룹 모으기
        tmp = deque()
        for r in range(11, -1, -1):
            if board[r][c] != '.':
                tmp.append(board[r][c])

        # 원래 위치 비우고 아래부터 채우기
        for r in range(11, -1, -1):
            board[r][c] = tmp.popleft() if tmp else '.'

ans = 0
while True:
    visited = [[False] * 6 for _ in range(12)]
    exploded = False

    # 터뜨릴 수 있는 모든 그룹 저장
    puyos = []
    for r in range(12):
        for c in range(6):
            if board[r][c] != '.' and not visited[r][c]:
                res = bfs(r, c, board[r][c])
                if res: puyos.extend(res)
    
    # 터뜨리기
    if puyos:
        exploded = True
        for pr, pc in puyos:
            board[pr][pc] = '.'
    
    if exploded:
        ans += 1
        down()
    else: break

print(ans)