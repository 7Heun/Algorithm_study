T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    arr90 = [[0] * N for _ in range(N)]
    arr180 = [[0] * N for _ in range(N)]
    arr270 = [[0] * N for _ in range(N)]

    '''
    90도 회전
    arr[i][j] -> arr[j][N-i-1]
    
    180도 회전
    arr[i][j] -> arr[N-i-1][N-j-1]
    
    270도 회전
    arr[i][j] -> arr[N-j-1][i]
    '''
    for i in range(N):
        for j in range(N):
            arr90[j][N-i-1] = arr[i][j]
            arr180[N-i-1][N-j-1] = arr[i][j]
            arr270[N-j-1][i] = arr[i][j]

    print(f"#{test_case}")
    for row in range(N):
        for n in arr90[row]:
            print(n, end='')
        print('', end=' ')
        for n in arr180[row]:
            print(n, end='')
        print('', end=' ')
        for n in arr270[row]:
            print(n, end='')
        print()
