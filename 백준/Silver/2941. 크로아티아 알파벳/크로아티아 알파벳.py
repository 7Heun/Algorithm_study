import sys
input = sys.stdin.readline

arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
string = list(input().strip())
now = ''
cnt = 0

for c in string:
    now += c
    if len(now) < 2: continue
    for i in range(len(arr)):
        if arr[i] in now:
            now = now.replace(arr[i], '')
            cnt += len(now) + 1
            now = ''
cnt += len(now)
print(cnt)