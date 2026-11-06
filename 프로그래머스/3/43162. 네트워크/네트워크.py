'''
dfs로 연결된 덩어리 개수 찾기
'''
import sys
sys.setrecursionlimit(10**6)

def dfs(start, computers, visited):
    stack = [start]
    while stack:
        now = stack.pop()
        visited[now] = 1
        for nxt in range(len(computers)):
            if not visited[nxt] and computers[now][nxt]:
                stack.append(nxt)

def solution(n, computers):
    ans = 0
    visited = [0 for _ in range(n)]
    for i in range(n):
        if visited[i]: continue
        dfs(i, computers, visited)
        ans += 1
    return ans
        