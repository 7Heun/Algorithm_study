def solution(n):
    ans = 0
    while n > 0:
        if n % 2 == 0:  # n이 짝수면 순간이동
            n //= 2
        else:   # n이 홀수면 점프
            n -= 1
            ans += 1
    return ans