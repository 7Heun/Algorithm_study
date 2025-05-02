from collections import deque
def solution(maps):
    n, m = len(maps), len(maps[0])
    queue = deque()
    queue.append((0, 0))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):  # 상하좌우 비교
            nx, ny = x + dx[i], y + dy[i]
            # 다음 좌표가 맵 밖이면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 다음 좌표가 벽이면 무시
            if maps[nx][ny] == 0:
                continue
            # 다음 좌표가 처음 가는 길이면 방문 표시
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1   # 최단거리 누적값 저장
                queue.append((nx, ny))
                
    return maps[-1][-1] if maps[-1][-1] > 1 else -1
      