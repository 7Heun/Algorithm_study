def solution(board):
    col = len(board)
    row = len(board[0])
    dp = [[0] * row for _ in range(col)]
    max_len = 0
    
    for i in range(col):
        for j in range(row):
            if board[i][j] == 1:
                if i == 0 or j == 0:    # 첫 행 또는 첫 열이면 1
                    dp[i][j] = 1
                else:   # 왼쪽 위, 왼쪽, 위 값 중 최솟값에 1 더한 값으로 업데이트
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                max_len = max(max_len, dp[i][j])
    return max_len ** 2
                        