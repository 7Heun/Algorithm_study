import sys
input = sys.stdin.readline
n, k = map(int, input().split())
medals = []
for _ in range(n):
    medals.append(list(map(int, input().split())))
rank = 1
for i in range(n):
    if medals[i][0] > medals[k-1][0]:
        rank += 1
    elif medals[i][0] == medals[k-1][0]:
        if medals[i][1] > medals[k-1][1]:
            rank += 1
        elif medals[i][1] == medals[k-1][1]:
            if medals[i][2] > medals[k-1][2]:
                rank += 1
print(rank)