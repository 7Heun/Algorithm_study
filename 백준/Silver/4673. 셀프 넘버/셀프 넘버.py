def d(n):
    return n + sum(map(int, str(n)))
arr = [0] * 10001
for i in range(1, 10001):
    if d(i) < 10001:
        arr[d(i)] = 1
for i in range(1, 10001):
    if arr[i] == 0:
        print(i)