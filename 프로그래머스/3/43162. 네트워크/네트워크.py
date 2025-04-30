def solution(n, computers):
    visited = [False] * n
    ans = 0
    
    def dfs(current):   # 방문 체크
        visited[current] = True
        for next in range(n):
            # 현재와 다음 노드가 연결되어 있고 다음 노드를 방문하지 않은 상태인 경우
            if computers[current][next] == 1 and not visited[next]:
                dfs(next)
                
    for i in range(n):
        if not visited[i]:
            dfs(i)
            ans += 1
    return ans