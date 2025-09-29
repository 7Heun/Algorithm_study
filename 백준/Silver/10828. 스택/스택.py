import sys
input = sys.stdin.readline
n = int(input())
stack = []
for _ in range(n):
    tmp = list(input().rstrip().split())
    if len(tmp) == 2:
        stack.append(int(tmp[1]))
        continue
    if tmp[0] == 'pop':
        print(stack.pop() if stack else -1)
    elif tmp[0] == 'size':
        print(len(stack))
    elif tmp[0] == 'empty':
        print(0 if stack else 1)
    elif tmp[0] == 'top':
        print(stack[-1] if stack else -1)
