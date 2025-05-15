from collections import deque
import sys
input = sys.stdin.readline

gears = [deque(input().strip()) for _ in range(4)]
K = int(input())

for _ in range(K):
    n, d = map(int, input().split())
    n -= 1
    to_rotate = [0] * 4
    to_rotate[n] = d

    # 왼쪽
    for i in range(n-1, -1, -1):
        if gears[i+1][6] == gears[i][2]: break
        to_rotate[i] = -to_rotate[i+1]

    # 오른쪽
    for i in range(n+1, 4):
        if gears[i-1][2] == gears[i][6]: break
        to_rotate[i] = -to_rotate[i-1]

    for n, d in enumerate(to_rotate):
        gears[n].rotate(d)

score = 0
for i in range(4):
    score += int(gears[i][0]) * (2 ** i)
print(score)