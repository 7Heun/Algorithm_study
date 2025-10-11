import sys
input = sys.stdin.readline

n = int(input())
exp = input().rstrip()
numbers = {}
for i in range(n):
    numbers[chr(ord('A') + i)] = int(input())

stack = []
for c in exp:
    if c.isalpha():
        stack.append(numbers[c])
    else:
        b = stack.pop()
        a = stack.pop()
        if c == '+':
            stack.append(a + b)
        elif c == '-':
            stack.append(a - b)
        elif c == '*':
            stack.append(a * b)
        elif c == '/':
            stack.append(a / b)

print(f"{stack[0]:.2f}")