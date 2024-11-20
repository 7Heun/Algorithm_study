'''
'('가 등장하면 스택에 저장하고, ')'가 등장하면 스택에서 요소를 꺼냄.
pop하는 시점에 스택이 비어있거나, s가 끝났을 때 스택이 비어있지 않으면 괄호의 짝이 맞지 않는 것이므로 False를 리턴함.
'''

def solution(s):
    stack = []
    for b in s:
        if b == "(":
            stack.append(b)
        else:
            if not stack:
                return False
            stack.pop()
    return False if stack else True