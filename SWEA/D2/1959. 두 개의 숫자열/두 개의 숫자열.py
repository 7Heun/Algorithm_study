T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))

    total = float('-inf')

    if N < M:
        for i in range(M - N + 1):
            tmp = 0
            for j in range(N):
                tmp += arr[j] * brr[i + j]
            total = max(total, tmp)
    else:
        for i in range(N - M + 1):
            tmp = 0
            for j in range(M):
                tmp += brr[j] * arr[i + j]
            total = max(total, tmp)

    print(f"#{test_case} {total}")