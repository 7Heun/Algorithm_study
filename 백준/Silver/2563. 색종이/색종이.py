import sys
input = sys.stdin.readline

n = int(input())
paper = [[0] * 100 for _ in range(100)]
for _ in range(n):
    x, y = map(int, input().split())
    for h in range(y, y+10):
        for w in range(x, x+10):
                if not paper[h][w]: paper[h][w] = 1
cnt = sum([row.count(1) for row in paper])
print(cnt)