def solution(n):
    answer = 1
    for i in range(1, n):
        if find_total(i, n):
            answer += 1
    return answer
    

def find_total(start, n):
    total = 0
    for i in range(start, n+1):
        if total == n:
            return True
        if total > n:
            return False
        total += i