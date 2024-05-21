import sys
input = sys.stdin.readline
n = int(input())
students = []
same_class = [0] * n
for i in range(n):
    students.append(list(map(int, input().split())))
    same_class[i] = [0] * n
for i in range(5):
    for j in range(n):
        for k in range(j+1, n):
            if students[j][i] == students[k][i]:
                same_class[j][k] = 1
                same_class[k][j] = 1
cnt = []
for i in range(n):
    cnt.append(sum(same_class[i]))
print(cnt.index(max(cnt))+1)