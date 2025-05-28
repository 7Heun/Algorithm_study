import sys
input = sys.stdin.readline

s = input().strip()
flag = 0
ans = ''
tmp = ''
for c in s:
    if flag:
        if c == '<':
            flag += 1
        elif c == '>':
            flag -= 1
        ans += c
        continue
    if c == ' ':
        ans += tmp[::-1]
        ans += ' '
        tmp = ''
        continue
    if c == '<':
        if tmp:
            ans += tmp[::-1]
            tmp = ''
        flag += 1
        ans += c
        continue
    tmp += c
if tmp:
    ans += tmp[::-1]
print(ans)         
