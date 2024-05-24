import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
res = []
for i in range(N-7):
    for j in range(M-7):
        cnt1 = 0
        cnt2 = 0
        for col in range(i, i+8):
            for row in range(j, j+8):
                if (col+row) % 2 == 0:
                    if board[col][row] != 'W':
                        cnt1 += 1
                    if board[col][row] != 'B':
                        cnt2 += 1
                else:
                    if board[col][row] != 'B':
                        cnt1 += 1
                    if board[col][row] != 'W':
                        cnt2 += 1
        res.append(min(cnt1, cnt2))
print(min(res))