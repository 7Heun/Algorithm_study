import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def pooling(matrix):
    # 2*2면 2번째로 큰 수 반환
    if len(matrix) == 2:
        flat = [a for r in matrix for a in r]
        flat.sort(reverse=True)
        return flat[1]

    # 4등분해서 각 부분에 대해 재귀 호출
    half = len(matrix) // 2
    top_left = [row[:half] for row in matrix[:half]]
    top_right = [row[half:] for row in matrix[:half]]
    bottom_left = [row[:half] for row in matrix[half:]]
    bottom_right = [row[half:] for row in matrix[half:]]
    
    result = [pooling(top_left), pooling(top_right), pooling(bottom_left), pooling(bottom_right)]

    # 2번째 큰 수 반환
    result.sort(reverse=True)
    return result[1]

print(pooling(arr))