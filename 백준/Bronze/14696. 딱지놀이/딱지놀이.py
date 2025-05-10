import sys
input = sys.stdin.readline

def check(a, b):
    for i in range(4, -1, -1):
        if a.count(i) > b.count(i):
            return "A"
        if a.count(i) < b.count(i):
            return "B"
    return "D"

N = int(input())
for _ in range(N):
    a = list(map(int, input().split()))[1:]
    b = list(map(int, input().split()))[1:]
    print(check(a, b))