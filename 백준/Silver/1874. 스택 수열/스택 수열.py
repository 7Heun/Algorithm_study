import sys
input = sys.stdin.readline

top = 1
stack = []
ans = []
flag = True
n = int(input())

for i in range (n):
    num = int(input())
    while top <= num:
        stack.append(top)
        ans.append('+')
        top += 1
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        flag = False
if flag:
    for a in ans:
        print(a)
else:
    print("NO")