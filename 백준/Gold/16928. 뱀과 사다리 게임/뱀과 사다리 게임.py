from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [i for i in range(101)]
for _ in range(N):
    x, y = map(int, input().split())
    board[x] = y
for _ in range(M):
    u, v = map(int, input().split())
    board[u] = v

visited = [0] * 101
pos = deque([1])
while pos:
    p = pos.popleft()
    for i in range(1, 7):
        np = p + i
        if np > 100: continue
        np = board[np]
        if not visited[np]:
            visited[np] = visited[p] + 1
            pos.append(np)
print(visited[100])