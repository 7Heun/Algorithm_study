from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    left = deque()
    right = deque()
    cmd = list(input().strip())
    for c in cmd:
        if c == '<':
            if left: right.appendleft(left.pop())
        elif c == '>':
            if right: left.append(right.popleft())
        elif c == '-':
            if left: left.pop()
        else:
            left.append(c)
    print("".join(left + right))