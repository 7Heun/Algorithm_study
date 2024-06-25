import sys
input = sys.stdin.readline 
N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings = sorted(meetings, key=lambda x: (x[1], x[0]))
cnt = 0; end = 0
for meeting in meetings:
    if meeting[0] >= end:
        cnt += 1
        end = meeting[1]
print(cnt)