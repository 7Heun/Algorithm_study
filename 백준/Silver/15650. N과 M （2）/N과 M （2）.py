import sys       
input = sys.stdin.readline
N, M = map(int, input().split())
result = []

def dfs(start, n, m):
    if m == 0:
        print(*result)
        return
    for i in range(start, n+1):
        result.append(i)
        dfs(i+1, n, m-1)
        result.pop()

dfs(1, N, M)