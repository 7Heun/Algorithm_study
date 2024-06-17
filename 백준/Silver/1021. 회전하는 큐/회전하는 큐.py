import sys
from collections import deque
input = sys.stdin.readline 

N, M = map(int, input().split())
indices = list(map(int, input().split()))
q = deque([i for i in range(1, N + 1)])
cnt = 0
idx = 0

while True:
    if indices[idx] == q[0]:
        q.popleft()
        idx += 1
        if idx == M:
            break
    else:
        if q.index(indices[idx]) <= len(q) // 2:
            q.append(q.popleft())
        else:
            q.appendleft(q.pop())
        cnt += 1

print(cnt)