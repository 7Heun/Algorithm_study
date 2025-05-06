import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
queue = deque([(n, 0)])
visited = [False] * 100001
visited[n] = True
while queue:
    x, cnt = queue.popleft()
    if x == k: break
    if 0 <= x + 1 <= 100000 and not visited[x+1]:
        visited[x+1] = True
        queue.append((x+1, cnt+1))
    if 0 <= x - 1 <= 100000 and not visited[x-1]:
        visited[x-1] = True
        queue.append((x-1, cnt+1))
    if 0 <= x * 2 <= 100000 and not visited[x*2]:
        visited[x*2] = True
        queue.append((x*2, cnt+1))
print(cnt)