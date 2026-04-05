from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

'''
dp[u][0]: u가 얼리 어답터가 아닌 경우 -> 자식 노드는 모두 얼리 어답터
dp[u][1]: u가 얼리 어답터인 경우 -> 자식 노드는 상관 x

dp[u][0] = sum(dp[v][1])
dp[u][1] = min(sum(dp[v][0] + dp[v][1])) + 1
'''

n = int(input())
graph = defaultdict(list)
dp = [[0] * 2 for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(now, parent):
    dp[now][0] = 0
    dp[now][1] = 1

    for nxt in graph[now]:
        if nxt == parent: continue
        dfs(nxt, now)
        dp[now][0] += dp[nxt][1]
        dp[now][1] += min(dp[nxt][0], dp[nxt][1])

dfs(1, 0)
print(min(dp[1][0], dp[1][1]))