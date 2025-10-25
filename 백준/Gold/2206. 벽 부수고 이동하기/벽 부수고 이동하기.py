import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

# visited[r][c][0]: 벽 안 부수고 방문
# visited[r][c][1]: 벽 부수고 방문
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1

    while q:
        r, c, flag = q.popleft()
        # 도착 체크
        if r == n - 1 and c == m - 1:
            return visited[r][c][flag]

        for i in range(4):
            nr, nc = r + dy[i], c + dx[i]
            if 0 <= nr < n and 0 <= nc < m:
                if graph[nr][nc] == 0 and not visited[nr][nc][flag]:
                    visited[nr][nc][flag] = visited[r][c][flag] + 1
                    q.append((nr, nc, flag))
                # 벽 부술 수 있으면 부수고 이동
                elif graph[nr][nc] == 1 and not flag:
                    visited[nr][nc][1] = visited[r][c][flag] + 1
                    q.append((nr, nc, 1))
    return -1

print(bfs())