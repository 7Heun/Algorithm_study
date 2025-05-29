from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
chickens = []
houses = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            chickens.append((i, j))
        elif board[i][j] == 1:
            houses.append((i, j))

combination = combinations(chickens, M)
min_d = float('inf')
for c in combination:
    sum_d = 0
    tmp_houses = deque(houses)
    while tmp_houses:
        d = float('inf')
        r1, c1 = tmp_houses.popleft()
        for r2, c2 in c:
            d = min(d, abs(r1-r2) + abs(c1-c2))
        sum_d += d
    min_d = min(min_d, sum_d)
print(min_d)