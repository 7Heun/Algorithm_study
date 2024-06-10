import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]
res = []
pointer = 0

for _ in range(N):
    pointer += K-1
    if pointer >= len(arr):
        pointer %= len(arr)
    res.append(arr.pop(pointer))

print('<', end='')
for i in range(N-1):
    print(res[i], end=', ')
print(res[-1], end='>')