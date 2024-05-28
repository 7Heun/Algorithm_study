import sys
input = sys.stdin.readline
N = int(input())

def g(n):
    result = 0
    for i in range(1, n+1):
        result += i * (n//i)
    return result

print(g(N))