import sys
input = sys.stdin.readline

N, K = map(int, input().split())
scores = [list(map(int, input().split())) for _ in range(N)]
scores.sort(key = lambda x: (x[1], x[2], x[3]), reverse=True)

idx = []
for i in range(N):
    if scores[i][0] == K:
        idx.append(i)
        rank = i+1
        break
for i in range(N):
    if i == idx[0]: continue
    if scores[idx[0]][1:] == scores[i][1:]:
        idx.append(i)
        rank = min(rank, i+1)
print(rank)