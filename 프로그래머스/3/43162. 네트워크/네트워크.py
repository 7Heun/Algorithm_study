'''
연결된 덩어리 찾기
dfs
'''
import sys
sys.setrecursionlimit(10**6)
from collections import deque
    
def dfs(now, n, computers, visited):
    visited[now] = True
    for nxt in range(n):
        if computers[now][nxt] == 1 and not visited[nxt]:
            dfs(nxt, n, computers, visited)
    
def solution(n, computers):
    visited = [False] * n
    ans = 0
    
    for i in range(n):
        # 방문 체크
        if not visited[i]:
            # 덩어리 찾기
            dfs(i, n, computers, visited)
            ans += 1
    return ans
            
            