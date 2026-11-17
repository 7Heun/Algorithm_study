T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

def check_board(board):
    # 행 체크
    for x in board:
        if len(set(x)) < 9: return 0
    # 열 체크
    for i in range(9):
        y_set = set()
        for j in range(9):
            y_set.add(board[j][i])
        if len(y_set) < 9: return 0
    # 박스 체크
    # 박스 기준 중앙에 도달하면 그 박스 체크
    dx = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    dy = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    for i in range(1, 9, 3):
        for j in range(1, 9, 3):
            box_set = set()
            for d in range(9):
                box_set.add(board[i+dx[d]][j+dy[d]])
            if len(box_set) < 9: return 0
    return 1

for test_case in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(9)]
    ans = check_board(board)
    print(f"#{test_case} {ans}")
