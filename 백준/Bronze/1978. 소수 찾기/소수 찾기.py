import sys
input = sys.stdin.readline
n = int(input())
l = list(map(int, input().split()))
cnt = 0

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for i in l:
    if is_prime(i):
        cnt += 1
print(cnt)