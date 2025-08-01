def solution(s):
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
            continue
        stack.append(c)
    return 0 if stack else 1