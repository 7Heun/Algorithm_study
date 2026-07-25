'''
BFS
상하좌우 4방향 탐색
장애물이나 가장자리에 부딪힐 때까지 미끄러져 움직임
bfs 4방향 탐색 돌 때 for문 안에서 변형
(x, y, cost)
'''
from collections import deque

def solution(board):
    start = (0, 0)
    N = len(board)
    M = len(board[0])
    # 시작점 찾아서 좌표 저장
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                start = (i, j, 0)
    
    dq = deque([start])
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    visited = [[False] * M for _ in range(N)]
    visited[start[0]][start[1]] = True
    n = 1
    while dq:
        cx, cy, cost = dq.popleft()
        # 종료 조건
        if board[cx][cy] == 'G': return cost
        for i in range(4):
            nx, ny = cx, cy

            # bfs 탐색
            # 보드판 경계나 벽에 부딪힐 때까지 움직임
            while True:
                if not (0 <= nx + dx[i] < N and 0 <= ny + dy[i] < M): break
                if board[nx + dx[i]][ny + dy[i]] == 'D': break
                nx += dx[i]
                ny += dy[i]
            
            # 부딪힌 곳이 방문한 적 없는 곳이면 dq에 넣음
            if not visited[nx][ny]:
                visited[nx][ny] = True
                dq.append((nx, ny, cost+1))

    return -1