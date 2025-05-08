import sys
input = sys.stdin.readline
N = int(input())
board = [[0] * 1001 for _ in range(1001)]
for i in range(1, N+1):
    x, y, w, h = map(int, input().split())
    for j in range(y, y+h):
        for k in range(x, x+w):
            board[j][k] = i

for i in range(1, N+1):
    print(sum(b.count(i) for b in board))