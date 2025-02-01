'''
스택을 하나 만들고, number를 순회한다.
현재 숫자가 스택의 마지막 숫자보다 크면 스택의 마지막 숫자를 현재 숫자로 바꾸고 k를 1 감소시킨다.
그렇지 않으면 그냥 현재 숫자를 스택에 추가한다.
number 순회가 끝난 뒤에도 k가 남으면, 뒤에서부터 k개의 숫자를 잘라낸다.
'''

def solution(number, k):
    stack = []
    for n in number:
        while stack and n > stack[-1] and k > 0:
            k -= 1
            stack.pop()
        stack.append(n)
    if k > 0:
        stack = stack[:-k]
    return ''.join(stack)