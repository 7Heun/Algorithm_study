def solution(land):
    n = len(land)
    for i in range(1, n):
        for j in range(4):  # 바로 위의 행에서 같은 열을 제외한 수 중 최댓값을 더함
            land[i][j] += max(land[i-1][k] for k in range(4) if k != j)
    return max(land[-1])    # 마지막 줄 중 최댓값 리턴