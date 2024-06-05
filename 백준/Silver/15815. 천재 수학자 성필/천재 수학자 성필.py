import sys
input = sys.stdin.readline

str = input().rstrip()
stack = []
for s in str:
    if s.isdigit():
        stack.append(s)
    else:
        a = stack.pop()
        b = stack.pop()
        cal = {
            '+': int(b) + int(a),
            '-': int(b) - int(a),
            '*': int(b) * int(a),
            '/': int(b) // int(a)
        }
        stack.append(cal[s])
print(stack[0])