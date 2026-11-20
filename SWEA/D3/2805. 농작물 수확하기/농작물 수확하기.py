T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    total = 0
    start, end = N // 2, N // 2 + 1

    for i in range(N // 2):
        total += sum(board[i][start:end])
        total += sum(board[N - i - 1][start:end])
        start -= 1
        end += 1

    total += sum(board[N//2])

    print(f"#{test_case} {total}")