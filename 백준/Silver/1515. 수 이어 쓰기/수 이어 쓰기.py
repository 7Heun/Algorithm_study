import sys
input = sys.stdin.readline

s = input().rstrip()
i, idx = 1, 0

while idx < len(s):
    for c in str(i):
        if idx < len(s) and s[idx] == c:
            idx += 1
    i += 1

print(i-1)