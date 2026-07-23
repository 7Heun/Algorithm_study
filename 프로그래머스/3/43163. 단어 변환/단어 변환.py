'''
최단거리니까 bfs가 좋을 것 같음
zip으로 몇 글자 다른지 비교
deque 만들고 depth 체크
'''
from collections import deque

# 한 글자만 다른지 비교하는 함수
def check(word1, word2):
    diff = 0
    for a, b in zip(word1, word2):
        if a != b: diff += 1
    return diff == 1

def solution(begin, target, words):
    # target이 words에 없으면 0 반환
    if target not in words: return 0
    visited = [False] * len(words)
    dq = deque([(begin, 0)])
    
    # bfs
    while dq:
        now_word, now_depth = dq.popleft()
        # target 되면 현재 depth 반환
        if now_word == target: return now_depth
        for i, next_word in enumerate(words):
            if visited[i]: continue
            # 한 글자만 다르면 dq에 넣기
            if check(now_word, next_word):
                visited[i] = True
                dq.append((next_word, now_depth + 1))
    # 변환 불가시 0 반환
    return 0