import sys
input = sys.stdin.readline

n = int(input())
i = now = 1
while now < n:
    now += 6 * i
    i += 1
print(i)