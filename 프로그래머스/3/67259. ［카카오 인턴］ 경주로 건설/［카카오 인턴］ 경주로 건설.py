'''
(0, 0) -> (N-1, N-1)
0으로만 이동 (1은 벽)
상하좌우 4방향 bfs 탐색
상하 or 좌우: 직선 도로 (100원)
코너 (500원)
직선도로 전체 + 거기서 생긴 코너
최소비용 return
cost[x][y][d]
'''
from collections import deque
import math

def solution(board):
    N = len(board)
    cost = [[[math.inf] * 4 for _ in range(N)] for _ in range(N)]
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    # (x, y, cost, d)
    dq = deque([(0, 0, 0, -1)])
    
    # 시작점 cost 처리
    for i in range(4):
        cost[0][0][i] = 0
    
    # bfs
    while dq:
        cx, cy, cc, cd = dq.popleft()
        
        # 이미 현재 cost가 더 높으면 무시
        if cd != -1 and cc > cost[cx][cy][cd]: continue

        # 목적지에 도달했으면 끝
        if cx == N-1 and cy == N-1: continue
        
        # 4방향 탐색
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            nd = i
            # board 바깥이면 무시
            if not (0 <= nx < N and 0 <= ny < N): continue
            # 벽(1)이면 무시
            if board[nx][ny] == 1: continue
            
            # cost 계산
            new_cost = cc
            
            # 방향 같으면 100원 추가, 다르면 100+500원 추가
            if not (cd == -1 or cd == nd):
                new_cost += 500
            new_cost += 100
            
            # 더 작은 cost 선택
            if new_cost <= cost[nx][ny][nd]:
                cost[nx][ny][nd] = new_cost
                dq.append((nx, ny, new_cost, nd))
    
    # 목적지 최소 비용 리턴
    return min(cost[N-1][N-1])