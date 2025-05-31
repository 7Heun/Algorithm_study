import sys
input = sys.stdin.readline

M = int(input())
s = set()
for _ in range(M):
    cmd = list(input().strip().split())
    if cmd[0] == 'add':
        s.add(int(cmd[1]))
    elif cmd[0] == 'remove':
        s.discard(int(cmd[1]))
    elif cmd[0] == 'check':
        print(1 if int(cmd[1]) in s else 0)
    elif cmd[0] == 'toggle':
        if int(cmd[1]) in s:
            s.remove(int(cmd[1]))
        else:
            s.add(int(cmd[1]))
    elif cmd[0] == 'all':
        s.update((i) for i in range(1, 21))
    elif cmd[0] == 'empty':
        s.clear()