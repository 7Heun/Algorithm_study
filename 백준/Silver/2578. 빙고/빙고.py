import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(5)]
call = [num for _ in range(5) for num in map(int, input().split())]
row_bingo = [False] * 5
col_bingo = [False] * 5
diag1_bingo = False
diag2_bingo = False
total = 0

for n in range(len(call)):
    for i in range(5):
        for j in range(5):
            if board[i][j] == call[n]:
                board[i][j] = 0
                if not row_bingo[i] and all(board[i][k] == 0 for k in range(5)):
                    row_bingo[i] = True
                    total += 1
                if not col_bingo[j] and all(board[k][j] == 0 for k in range(5)):
                    col_bingo[j] = True
                    total += 1
                if i == j and not diag1_bingo and all(board[k][k] == 0 for k in range(5)):
                    diag1_bingo = True
                    total += 1
                if i + j == 4 and not diag2_bingo and all(board[k][4-k] == 0 for k in range(5)):
                    diag2_bingo = True
                    total += 1
                if total >= 3:
                    print(n + 1)
                    exit()
                break
