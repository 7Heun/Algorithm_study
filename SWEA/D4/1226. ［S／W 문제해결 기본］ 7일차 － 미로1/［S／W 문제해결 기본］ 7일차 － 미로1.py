from collections import deque

def check(board):
    dq = deque([(1, 1)])
    visited = [[False] * 16 for _ in range(16)]
    visited[1][1] = True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while dq:
        x, y = dq.popleft()
        if board[x][y] == 3: return 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 16 and 0 <= ny < 16 and not visited[nx][ny] and board[nx][ny] != 1:
                visited[nx][ny] = True
                dq.append((nx, ny))
    return 0


for test_case in range(10):
    T = int(input())
    board = [list(map(int, input())) for _ in range(16)]
    print(f"#{T} {check(board)}")