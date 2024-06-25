import sys
input = sys.stdin.readline 
N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)
res = 0
for i in range(N):
    res += a[i] * b[i]
print(res)