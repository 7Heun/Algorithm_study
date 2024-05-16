import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = [i for i in range(2, n+1)]
cnt = 0
while True:
    p = arr[0]
    for i in arr:
        if i % p == 0:
            arr.remove(i)
            cnt += 1
            if cnt == k:
                print(i)
                exit()