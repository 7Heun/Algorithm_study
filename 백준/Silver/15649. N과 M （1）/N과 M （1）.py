N, M = map(int, input().split())

def dfs(n, m, result=[]):
    if m == 0:
        print(*result)
        return
    for i in range(1, n+1):
        if i not in result:
            result.append(i)
            dfs(n, m-1, result)
            result.pop()

dfs(N, M)