def solution(triangle):
    n = len(triangle)
    for i in range(1, n):
        for j in range(i+1):
            if j == 0:  # 제일 왼쪽 수는 오른쪽 위에서만 올 수 있음
                triangle[i][j] += triangle[i-1][j]
            elif j == i:    # 제일 오른쪽 수는 왼쪽 위에서만 올 수 있음
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
    return max(triangle[-1])    # 마지막 줄에서 가장 큰 수 리턴