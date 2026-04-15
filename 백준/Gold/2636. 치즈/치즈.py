from collections import deque
import sys
input = sys.stdin.readline

'''
bfs
치즈 좌표 파악, 바깥쪽으로만 전파 
가장자리는 테두리 (치즈 x)
=> 가장자리 공기에서 시작해서 치즈 탐색
'''
r, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]

rows = [0, 1, 0, -1]
cols = [1, 0, -1, 0]

def bfs():
    # 한시간마다 (0, 0)에서 탐색 시작
    dq = deque([(0, 0)])
    visited = [[0] * c for _ in range(r)]
    visited[0][0] = 1
    melted = 0  # 녹은 치즈 개수

    while dq:
        cr, cc = dq.popleft()
        for d in range(4):
            nr, nc = cr + rows[d], cc + cols[d]

            # 위치, 방문 여부 체크
            if not (0 <= nr < r and 0 <= nc < c): continue
            if visited[nr][nc]: continue

            visited[nr][nc] = 1
            
            # 바깥 공기 만나면 dq에 넣기
            if board[nr][nc] == 0:
                dq.append((nr, nc))
            
            # 치즈 만나면 녹이기
            else:
                board[nr][nc] = 0
                melted += 1

    return melted

time = 0
cnt = 0

while True:
    melted = bfs()

    # 치즈 다 녹으면 종료
    if melted == 0: break

    # 치즈 개수, 시간 갱신
    cnt = melted
    time += 1

print(time)
print(cnt)