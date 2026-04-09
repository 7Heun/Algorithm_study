import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

'''
출발점 고정하고 dfs로 사이클 찾기
cur: 현재위치, visited: 방문한 도시 상태 (비트마스크)
dp[cur][visited]: 현재 상태에서 남은 도시를 다 돌고 시작점으로 가는 최소 비용
'''

n = int(input())
weights = [list(map(int, input().split())) for _ in range(n)]
INF = float('inf')
dp = [[-1] * (1 << n) for _ in range(n)]

def dfs(cur, visited):
    # 현재 시작점 기준 모든 도시 방문하면 시작점으로                           
    if visited == (1 << n) - 1:
        return weights[cur][0] if weights[cur][0] else INF
    
    # 이미 계산된 값 있으면 그대로 사용
    if dp[cur][visited] != -1:
        return dp[cur][visited]
    
    dp[cur][visited] = INF
    
    for nxt in range(n):
        # 이미 방문한 도시면 스킵
        if visited & (1 << nxt): continue
        # 못 가면 스킵
        if weights[cur][nxt] == 0: continue

        dp[cur][visited] = min(
            dp[cur][visited],
            weights[cur][nxt] + dfs(nxt, visited | (1 << nxt)))
    
    return dp[cur][visited]

print(dfs(0, 1 << 0))