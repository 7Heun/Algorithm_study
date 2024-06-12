import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
deq = deque()
for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'push_front':
        deq.appendleft(cmd[1])
    elif cmd[0] == 'push_back':
        deq.append(cmd[1])
    elif cmd[0] == 'pop_front':
        print(deq.popleft() if deq else -1)
    elif cmd[0] == 'pop_back':
        print(deq.pop() if deq else -1)
    elif cmd[0] == 'size':
        print(len(deq))
    elif cmd[0] == 'empty':
        print(0 if deq else 1)
    elif cmd[0] == 'front':
        print(deq[0] if deq else -1)
    else:
        print(deq[-1] if deq else -1)