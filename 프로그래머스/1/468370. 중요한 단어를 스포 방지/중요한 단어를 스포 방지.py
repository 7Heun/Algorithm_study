'''
각 스포일러 위치 파악
단어 위치와 겹치는지 확인
=> 단어를 분리하면서 각 단어가 스포일러인지 표시
'''

def solution(message, spoiler_ranges):
    words = message.split(" ")
    idx = 0
    
    # 스포일러 단어와 평문 단어 나눠서 저장
    spoiler_words = set()
    normal_words = set()
    
    for word in words:
        start = idx
        end = start + len(word) - 1
        is_spoiler = False
        
        for s, e in spoiler_ranges:
            # 현재 구간이 스포일러 구간과 겹치는지 확인
            if start <= e and end >= s:
                is_spoiler = True
                break
        if is_spoiler:
            spoiler_words.add(word)
        else:
            normal_words.add(word)
        
        idx = end + 2
    
    # 스포일러 단어 중에 중복 없는 단어 개수 리턴
    return len(spoiler_words - normal_words)