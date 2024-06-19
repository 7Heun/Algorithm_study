import sys
input = sys.stdin.readline 
N = int(input())
P = list(map(int, input().split()))
P.sort()
ans = [0] * N
for i in range(N):
    ans[i] = sum(P[:i+1])
print(sum(ans))