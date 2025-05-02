# 나중에 다시
def solution(n, m, x, y, r, c, k):
    shortest = abs(x-r) + abs(y-c)
    if shortest > k or shortest % 2 != k % 2: return 'impossible'
    extra = k - shortest
    curr_x, curr_y = max(x, r), min(c, y)
    answer = 'd' * max(r - x, 0)
    last_u = 0
    last_r = 0
    while curr_x < n and extra:
        answer += 'd'
        curr_x += 1
        last_u += 1
        extra -= 2
    answer += 'l' * max(y - c, 0)
    while curr_y > 1 and extra:
        answer += 'l'
        curr_y -= 1
        last_r += 1
        extra -= 2
    loop = 'rl'
    if curr_y == m: loop = 'lr'
    while extra: 
        answer += loop
        extra -= 2
    answer += 'r' * (max(c - y, 0) + last_r)
    answer += 'u' * (max(x - r, 0) + last_u)
    return answer