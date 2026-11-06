'''
dfs로 백트래킹
bfs로 감염
'''
from collections import deque
import sys
sys.setrecursionlimit(10**6)    

def solution(n, infection, edges, k):
    answer = 0
    graph = [[] for _ in range(n + 1)]

    for x, y, pipe_type in edges:
        graph[x].append((y, pipe_type))
        graph[y].append((x, pipe_type))
    
    # 감염
    def spread(pipe, infected):
        dq = deque()
        for i in range(len(infected)):
            if infected[i]: dq.append(i)
        while dq:
            now = dq.popleft()
            for nxt, pipe_type in graph[now]:
                if not infected[nxt] and pipe == pipe_type:
                    infected[nxt] = True
                    dq.append(nxt)
    
    # 감염 개수 구하기
    def simulate(path):
        infected = [False] * (n + 1)
        infected[infection] = True
        for pipe in path:
            spread(pipe, infected)
        return sum(infected)
    
    # 전체 돌면서 최대 감염 개수 구하기
    def dfs(depth, path):
        nonlocal answer
        if depth == k:
            count = simulate(path)
            answer = max(answer, count)
            return
        for pipe in range(1, 4):
            path.append(pipe)
            dfs(depth+1, path)
            path.pop()
            
    dfs(0, [])
    return answer         
            