from collections import deque
import sys
input = sys.stdin.readline

'''
1. time += 1
2. head 꺼내기
3. 이동
4. 범위 체크
5. 충돌 체크
6. snake.append
7. 사과 있으면 유지
8. 사과 없으면 tail 제거
9. 방향 전환
'''
n = int(input())
k = int(input())
apples = set(tuple(map(int, input().split())) for _ in range(k))
l = int(input())
turns = {}
for _ in range(l):
    x, c = input().split()
    turns[int(x)] = c

snake = deque([(1, 1)])
visited = set()
visited.add((1, 1))
time = 0

# 왼쪽(L) 90도 회전이면 -1, 반대면 +1
rows = [0, 1, 0, -1]
cols = [1, 0, -1, 0]
d = 0
while True:
    time += 1
    # 머리 위치 꺼내기
    cr, cc = snake[-1]
    # 이동
    nr, nc = cr + rows[d], cc + cols[d]

    # 범위 체크
    if not (1 <= nr <= n and 1 <= nc <= n): break
    # 충돌 체크
    if (nr, nc) in visited: break
    
    # 이동
    snake.append((nr, nc))
    visited.add((nr, nc))
    
    # 사과 체크
    if (nr, nc) in apples:
        apples.remove((nr, nc))
    else:
        tail = snake.popleft()
        visited.remove(tail)

    # 방향 전환
    if time in turns: 
        if turns[time] == 'L':
            d = 3 if d == 0 else d-1
        else:
            d = 0 if d == 3 else d+1
    
print(time)