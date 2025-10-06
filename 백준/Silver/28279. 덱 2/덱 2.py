import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
dq = deque()
for _ in range(n):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        dq.appendleft(cmd[1])
    elif cmd[0] == 2:
        dq.append(cmd[1])
    elif cmd[0] == 3:
        print(dq.popleft() if dq else -1)
    elif cmd[0] == 4:
        print(dq.pop() if dq else -1)
    elif cmd[0] == 5:
        print(len(dq))
    elif cmd[0] == 6:
        print(0 if dq else 1)
    elif cmd[0] == 7:
        print(dq[0] if dq else -1)
    else:
        print(dq[-1] if dq else -1)