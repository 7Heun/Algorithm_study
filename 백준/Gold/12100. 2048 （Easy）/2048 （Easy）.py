import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

def move_left(board):
    new_board = []
    for row in board:
        new_row = [r for r in row if r != 0]    #  빈칸 제거
        result = []
        skip = False
        for i in range(len(new_row)):
            if skip:
                skip = False
                continue
            if i+1 < len(new_row) and new_row[i] == new_row[i+1]:
                result.append(new_row[i] * 2)
                skip = True
            else:
                result.append(new_row[i])
        result += [0] * (len(row) - len(result))
        new_board.append(result)
    return new_board

def rotate(board):
    new_board = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_board[j][N-i-1] = board[i][j]
    return new_board

def dfs(board, depth):
    if depth == 5:
        return max(map(max, board))
    result = 0
    for i in range(4):
        rotated_board = [row[:] for row in board]
        for _ in range(i):
            rotated_board = rotate(rotated_board)
        next_board = move_left(rotated_board)
        
        result = max(result, dfs(next_board, depth+1))
    return result

ans = dfs(board, 0)
print(ans)
