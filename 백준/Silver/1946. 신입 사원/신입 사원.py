import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    score = [list(map(int, input().split())) for _ in range(N)]
    score.sort()
    cnt = 1
    min_score = score[0][1]
    for i in range(1, N):
        if score[i][1] < min_score:
            cnt += 1
            min_score = score[i][1]
    print(cnt)