import sys
input = sys.stdin.readline

exp = input().rstrip()

sep = exp.split('-')
sums = [sum(map(int, s.split('+'))) for s in sep]

ans = sums[0] - sum(sums[1:])
print(ans)