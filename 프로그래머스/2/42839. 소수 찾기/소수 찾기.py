'''
numbers로 만들 수 있는 모든 조합을 만들어 소수인지 판별한다.
만들어진 숫자가 소수면 arr 배열에 추가하고, set을 사용해 중복을 제거한다.
arr의 길이를 리턴한다.
'''

from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    arr = []
    for i in range(1, len(numbers)+1):
        for j in permutations(numbers, i):
            n = int("".join(j))
            if is_prime(n):
                arr.append(n)
    return len(set(arr))