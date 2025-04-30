def solution(begin, target, words):
    # 서로 한 글자만 다른 단어인지 체크하는 함수
    def is_one_diff(word1, word2):
        diff_cnt = 0
        for w1, w2 in zip(word1, word2):
            if w1 != w2:
                diff_cnt += 1
        return True if diff_cnt == 1 else False
    
    visited = [False] * len(words)
    ans = float('inf')
    
    def dfs(word, cnt):
        nonlocal ans
        # target 만들어졌으면 가장 짧은 단계수 업데이트
        if word == target:
            ans = min(ans, cnt)
            return
        # words 순회하며 한 글자만 다른 단어 찾아서 내려감
        for i, w in enumerate(words):
            if not visited[i] and is_one_diff(word, w):
                visited[i] = True
                dfs(w, cnt+1)
                visited[i] = False
            
    dfs(begin, 0)
    return ans if ans != float('inf') else 0