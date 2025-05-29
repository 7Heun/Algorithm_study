import sys
input = sys.stdin.readline

string = list(input().strip())
bomb = input().strip()
stack = []

for s in string:
    stack.append(s)
    if len(stack) >= len(bomb):
        if ''.join(stack[-len(bomb):]) == bomb:
            for _ in range(len(bomb)): stack.pop()
            
print(''.join(stack) if stack else "FRULA")
