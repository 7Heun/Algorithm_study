def dfs(r):
    global ans

    # 행 전부 탐색하면 끝
    if r == N:
        ans += 1
        return

    for c in range(N):
        flag = True
        # (r, c)에 배치 가능한지 확인
        for pr in range(r):
            pc = queens[pr]
            if pc == c or abs(pr-r) == abs(pc-c):
                flag = False
                break
        if flag:
            queens[r] = c
            dfs(r + 1)
            queens[r] = -1

T = int(input())
for x in range(1, T + 1):
    N = int(input())
    ans = 0
    queens = [-1] * N
    dfs(0)
    print(f"#{x} {ans}")