import sys
input = sys.stdin.readline

N = int(input())
cookie = [list(input().strip()) for _ in range(N)]

def find_heart():
    for i in range(1, N-1):
        cnt = 0
        for j in range(1, N-1):
            if cookie[i][j] == '_':
                continue
            cnt += 1
            if cnt >= 2:
                if cookie[i-1][j] == '*' and cookie[i+1][j] == '*':
                    return (i, j)

heart_x, heart_y = find_heart()
# 왼팔, 오른팔, 허리, 왼다리, 오른다리
left_arm = cookie[heart_x][:heart_y].count('*')
right_arm = cookie[heart_x][heart_y+1:].count('*')
waist = left_leg = right_leg = 0

for i in range(heart_x + 1, N):
    if cookie[i][heart_y] != '*':
        break
    waist += 1

for i in range(heart_x + waist + 1, N):
    if cookie[i][heart_y-1] == '*':
        left_leg += 1
    if cookie[i][heart_y+1] == '*':
        right_leg += 1

print(heart_x+1, heart_y+1)
print(left_arm, right_arm, waist, left_leg, right_leg)
