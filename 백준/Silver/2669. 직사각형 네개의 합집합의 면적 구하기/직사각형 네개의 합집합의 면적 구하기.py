import sys
input = sys.stdin.readline

arr = [[0] * 101 for _ in range(101)]
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1
    
print(sum(a.count(1) for a in arr))