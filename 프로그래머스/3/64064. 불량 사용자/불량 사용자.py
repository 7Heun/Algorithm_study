def solution(user_id, banned_id):
    # user_id가 banned_id 패턴에 걸리는지 체크하는 함수
    def check(user, banned):
        if len(user) != len(banned):    # 길이 다르면 False
            return False
        for u, b in zip(user, banned):  # 각 글자가 다르고 '*'도 아니면 False
            if b != '*' and u != b:
                return False
        return True

    result = set()  # 중복 제거용
    visited = [False] * len(user_id)
    
    # banned_id에 걸리는 user_id가 나오면 다음 banned_id로 넘어가는 방식으로 dfs 순회
    def dfs(idx, comb, visited):
        if idx == len(banned_id):
            # 중복 제거를 위해 정렬 후 set에 추가하기 위해 tuple로 변환
            result.add(tuple(sorted(comb)))
            return
        for current, userid in enumerate(user_id):
            # 현재 user_id가 banned_id에 걸리면 다음 banned_id로 이동 (dfs)
            if not visited[current] and check(userid, banned_id[idx]):
                visited[current] = True
                dfs(idx+1, comb+[userid], visited)
                visited[current] = False
    dfs(0, [], visited)
    return len(result)
    
            