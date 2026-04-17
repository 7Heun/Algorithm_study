from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    pri = deque(list(map(int, input().split())))
    que = deque(list(range(n)))
    cnt = 0
    while pri:
        if pri[0] == max(pri):
            cnt += 1
            pri.popleft()
            if que.popleft() == m:
                print(cnt)
        else:
            pri.rotate(-1)
            que.rotate(-1)
