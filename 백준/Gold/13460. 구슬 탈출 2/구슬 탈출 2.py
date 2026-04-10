from collections import deque
import sys
input = sys.stdin.readline

'''
구슬(시작점) 위치 찾아서 bfs
파란 구슬, 빨간 구슬 같이 탐색
이동 횟수 10번 넘으면 -1, 아니면 이동 횟수 출력
아니면 deque에 이동 횟수를 포함해서 저장
'''

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

rows = [0, 0, -1, 1]
cols = [1, -1, 0, 0]

# 구슬 위치 찾기
def find_start(color):
    for i in range(1, n-1):
        for j in range(1, m-1):
            if board[i][j] == color:
                return (i, j)

# 구슬 이동
def move(r, c, dr, dc):
    dist = 0
    is_hole = False
    while True:
        nr, nc = r + dr, c + dc
        # 벽이면 멈춤
        if board[nr][nc] == '#': break
        # 이동
        r, c = nr, nc
        dist += 1
        # 구멍에 빠지면 끝
        if board[r][c] == 'O': 
            is_hole = True
            break
    return r, c, dist, is_hole

red_r, red_c = find_start('R')
blue_r, blue_c = find_start('B')
dq = deque([(red_r, red_c, blue_r, blue_c, 0)])
visited = set()
visited.add((red_r, red_c, blue_r, blue_c))

# bfs
while dq:
    crr, crc, cbr, cbc, dist = dq.popleft()
    for d in range(4):
        # 방향에 따라 red, blue 이동 순서 정하기
        # 오른쪽
        if d == 0:
            if crc < cbc:
                nrr, nrc, red_dist, red_hole = move(crr, crc, rows[d], cols[d])
                nbr, nbc, blue_dist, blue_hole = move(cbr, cbc, rows[d], cols[d])
            else:
                nbr, nbc, blue_dist, blue_hole = move(cbr, cbc, rows[d], cols[d])
                nrr, nrc, red_dist, red_hole = move(crr, crc, rows[d], cols[d])
        # 왼쪽
        elif d == 1:
            if crc > cbc:
                nbr, nbc, blue_dist, blue_hole = move(cbr, cbc, rows[d], cols[d])
                nrr, nrc, red_dist, red_hole = move(crr, crc, rows[d], cols[d])
            else:
                nrr, nrc, red_dist, red_hole = move(crr, crc, rows[d], cols[d])
                nbr, nbc, blue_dist, blue_hole = move(cbr, cbc, rows[d], cols[d])
        # 위쪽:
        elif d == 2:
            if crr < cbr:
                nbr, nbc, blue_dist, blue_hole = move(cbr, cbc, rows[d], cols[d])
                nrr, nrc, red_dist, red_hole = move(crr, crc, rows[d], cols[d])
            else:
                nrr, nrc, red_dist, red_hole = move(crr, crc, rows[d], cols[d])
                nbr, nbc, blue_dist, blue_hole = move(cbr, cbc, rows[d], cols[d])
        # 아래쪽:
        else:
            if crr > cbr:
                nbr, nbc, blue_dist, blue_hole = move(cbr, cbc, rows[d], cols[d])
                nrr, nrc, red_dist, red_hole = move(crr, crc, rows[d], cols[d])
            else:
                nrr, nrc, red_dist, red_hole = move(crr, crc, rows[d], cols[d])
                nbr, nbc, blue_dist, blue_hole = move(cbr, cbc, rows[d], cols[d])
        
        # 구슬 겹칠 때 처리
        if (nrr, nrc) == (nbr, nbc):
            # 더 멀리 온 애가 더 뒤에서 온 것 -> 한 칸 뒤로
            if red_dist > blue_dist:
                # red 한 칸 뒤로
                nrr -= rows[d]
                nrc -= cols[d]
                red_dist -= 1
            else:
                # blue 한 칸 뒤로
                nbr -= rows[d]
                nbc -= cols[d]
        # blue가 먼저 구멍에 들어가면 실패
        if blue_hole: continue
        # red가 구멍 들어가면 성공
        if red_hole:
            print(dist+1 if dist+1 <= 10 else -1)
            exit()

        # 이동 횟수 10번 초과시 실패
        if dist >= 10: continue
        # 방문 처리
        if (nrr, nrc, nbr, nbc) not in visited:
            visited.add((nrr, nrc, nbr, nbc))
            dq.append((nrr, nrc, nbr, nbc, dist+1))
print(-1)