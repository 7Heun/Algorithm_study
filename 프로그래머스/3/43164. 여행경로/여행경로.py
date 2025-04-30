def solution(tickets):
    tickets.sort()  # 티켓 경로 알파벳순 정렬
    visited = [False] * len(tickets)
    ans = []
    def dfs(route):
        # 티켓을 모두 사용하면 종료 (방문지 총 개수 == 티켓 수 + 1)
        if len(route) == len(tickets) + 1:
            ans.append(route)
            return
        for i, [s, d] in enumerate(tickets):
            # 현재 위치에서 출발하는 티켓인 경우 dfs 탐색
            if not visited[i] and s == route[-1]:
                visited[i] = True
                dfs(route + [d])
                visited[i] = False
    dfs(["ICN"])
    return ans[0]   # 알파벳순 첫번째 경로 리턴
            