import sys       
input = sys.stdin.readline
N = int(input())
arr = [i for i in range(1, N+1)]
visited = [False] * N
result = []

def dfs(depth):
    if depth == N:
        print(' '.join(map(str, result)))
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            result.append(arr[i])
            dfs(depth+1)
            result.pop()
            visited[i] = False
dfs(0)