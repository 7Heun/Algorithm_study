import sys
input = sys.stdin.readline

arr = {}
for i in range(1, 9):
    n = int(input())
    arr[n] = i

sorted_arr = sorted(arr.items(), key=lambda x: -x[0])
top5 = sorted_arr[:5]

score = 0
idx = []
for s, i in sorted(top5, key=lambda x: x[1]):
    score += s
    idx.append(i)
print(score)
print(*idx)