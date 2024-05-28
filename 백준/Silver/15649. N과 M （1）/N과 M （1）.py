import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())

def dfs(depth, n, m, result=deque()):
    if depth == m:
        print(*result)
        return
    for i in range(n):
        if i+1 not in result:
            result.append(i+1)
            dfs(depth+1, n, m, result)
            result.pop()
dfs(0, N, M)