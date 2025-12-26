import sys
input = sys.stdin.readline

# p(n) = p(n-5) + p(n-1)
p = [0] * 101
p[1] = p[2] = p[3] = 1
p[4] = 2
for i in range(5, 101):
    p[i] = p[i-5] + p[i-1]

t = int(input())
for _ in range(t):
    n = int(input())
    print(p[n])
