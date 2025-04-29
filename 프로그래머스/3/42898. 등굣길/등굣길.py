def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]    # 전체 좌표의 가능한 경로 수를 0으로 초기화
    for i in range(n):
        for j in range(m):
            if [j+1, i+1] in puddles:   # 현재 좌표가 물에 잠긴 경우 건너뜀
                continue
            if i == 0 and j == 0:    # 시작점은 가능한 경로 수 1
                dp[i][j] = 1
            elif i == 0:    # 현재 좌표가 0번째 행이면 왼쪽에서만 올 수 있음
                dp[i][j] = dp[i][j-1]
            elif j == 0:
                dp[i][j] = dp[i-1][j]   # 현재 좌표가 0번째 열이면 위에서만 올 수 있음
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]  # 현재 좌표의 위와 왼쪽의 경로 수 더함
    return dp[-1][-1] % 1000000007