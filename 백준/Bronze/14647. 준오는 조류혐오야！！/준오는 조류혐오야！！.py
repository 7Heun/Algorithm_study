import sys
input = sys.stdin.readline
n, m = map(int, input().split())
cnt_9 = 0
row = [0]*n
col = [0]*m
for i in range(n):
    bingo = list(map(str, input().split()))
    for j in range(m):
        row[i] += bingo[j].count('9')
        col[j] += bingo[j].count('9')
        cnt_9 += bingo[j].count('9')
print(cnt_9 - max(max(row), max(col)))