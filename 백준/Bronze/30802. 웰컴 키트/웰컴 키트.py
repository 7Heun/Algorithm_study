import sys
input = sys.stdin.readline
N = int(input())
tshirt = list(map(int, input().split()))
T, P = map(int, input().split())

t_count = 0
for t in tshirt:
    t_count += t//T if t%T==0 else t//T+1
print(t_count)
print(N//P, N%P)