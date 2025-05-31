import sys, bisect
input = sys.stdin.readline

N, M = map(int, input().split())
titles = []
powers = []
for _ in range(N):
    t, p = input().strip().split()
    titles.append(t)
    powers.append(int(p))

for _ in range(M):
    power = int(input())
    idx = bisect.bisect_left(powers, power)
    print(titles[idx])