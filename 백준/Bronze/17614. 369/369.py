import sys
input = sys.stdin.readline
n = int(input())
cnt = 0
for i in range(1, n+1):
    cnt += str(i).count('3') + str(i).count('6') + str(i).count('9')
print(cnt)