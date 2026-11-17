T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T + 1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]
    x, y = 0, 0

    # 하 -> 우 -> 상 -> 좌
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    d = 0

    for now in range(1, N*N+1):
        snail[x][y] = now

        nx = x + dx[d]
        ny = y + dy[d]

        if not (0 <= nx < N and 0 <= ny < N and not snail[nx][ny]):
            d = (d+1) % 4
            nx = x + dx[d]
            ny = y + dy[d]
        x, y = nx, ny

    print(f"#{test_case}")
    for s in snail:
        print(*s)