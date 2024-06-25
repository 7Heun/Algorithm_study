import sys
input = sys.stdin.readline 
s = input().strip().split('-')
res = 0
for i in s[0].split('+'):
    res += int(i)
for i in s[1:]:
    for j in i.split('+'):
        res -= int(j)
print(res)