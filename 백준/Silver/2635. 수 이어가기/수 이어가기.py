import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(1, n+1):
    tmp = []
    tmp.append(n)
    tmp.append(i)
    idx = 1
    while True:
        if tmp[idx-1] - tmp[idx] < 0:
            if len(tmp) > len(arr):
                arr = tmp.copy()
            break
        tmp.append(tmp[idx-1] - tmp[idx])
        idx += 1
print(len(arr))
print(*arr)