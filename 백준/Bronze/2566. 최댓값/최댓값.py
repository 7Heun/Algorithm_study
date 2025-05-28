import sys
input = sys.stdin.readline

a, b = -1, -1
m = -1
for i in range(9):
    tmp = list(map(int, input().split()))
    for j in range(9):
        if tmp[j] > m:
            m = tmp[j]
            a, b = i+1, j+1
print(m)
print(a, b)