from collections import deque
def bfs(start, target, maps):
    queue = deque()
    queue.append(start)
    n, m = len(maps), len(maps[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = [[0] * m for _ in range(n)]
    while queue:
        x, y = queue.popleft()
        for i in range(4): # 상하좌우 탐색
            nx, ny = x + dx[i], y + dy[i]
            # 다음 좌표가 미로 밖이면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 다음 좌표가 벽이거나 이미 방문한 곳이면 무시
            if maps[nx][ny] == "X" or visited[nx][ny]:
                continue
            visited[nx][ny] = visited[x][y] + 1
            # 목표 지점에 도달하면 최단거리 반환
            if maps[nx][ny] == target:
                return visited[nx][ny]
            queue.append((nx, ny))
    return -1

# 목표 지점의 좌표를 반환하는 함수
def find_target(target, maps):
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == target:
                return (i, j)
            
def solution(maps):
    start = find_target("S", maps)
    lever = find_target("L", maps)
    to_lever = bfs(start, "L", maps)
    to_exit = bfs(lever, "E", maps)
    if to_lever == -1 or to_exit == -1:
        return -1
    return to_lever + to_exit