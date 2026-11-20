def check(start, s):
    if len(s) == 7:
        ans.add(s)
        return

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    x, y = start
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < 4 and 0 <= ny < 4:
            check((nx, ny), s + board[nx][ny])

T = int(input())
for test_case in range(1, T + 1):
    board = [input().split() for _ in range(4)]
    ans = set()
    for i in range(4):
        for j in range(4):
            check((i, j), board[i][j])
    print(f"#{test_case} {len(ans)}")