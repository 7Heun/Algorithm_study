import sys
input = sys.stdin.readline

'''
상하좌우 이동, 같은 숫자 나오면 합치기
-> board rotate 시켜서 한 방향으로만 이동
dfs로, depth 체크 (최대 5번 이동)
'''
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

def move_left(board):
    new_board = []
    for row in board:
        # 빈칸 제거
        new_row = [r for r in row if r != 0]
        # 숫자 비교
        result = []
        idx = 0
        while idx < len(new_row)-1:
            if new_row[idx] == new_row[idx+1]:
                result.append(new_row[idx]*2)
                idx += 2
            else:
                result.append(new_row[idx])
                idx += 1
        # 마지막 숫자 처리
        if idx == len(new_row)-1:
            result.append(new_row[idx])
        result += [0] * (len(row) - len(result))
        new_board.append(result)
    return new_board

def rotate(board):
    new_board = [[0] * n for _ in range(n)]
    # 90도 회전
    for i in range(n):
        for j in range(n):
            new_board[n-j-1][i] = board[i][j]
    return new_board

def dfs(board, depth):
    if depth == 5:
        return max(map(max, board))
    result = 0
    for i in range(4):
        # board 복사
        rotated_board = [row[:] for row in board]
        # 회전
        for _ in range(i):
            rotated_board = rotate(rotated_board)
        # 숫자 합치기
        next_board = move_left(rotated_board)
        result = max(result, dfs(next_board, depth+1))
    return result

print(dfs(board, 0))
