import sys
input = sys.stdin.readline

n = int(input())
expected = [int(input()) for _ in range(n)]
expected.sort()

total = 0
for i in range(n):
    total += abs(expected[i] - (i+1))
print(total)