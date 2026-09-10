def solution(num):
    t = 0
    while t < 500:
        if num == 1: return t
        t += 1
        is_even = True if num % 2 == 0 else False
        if is_even:
            num //= 2
        else:
            num = num * 3 + 1
    return t if num == 1 else -1
    