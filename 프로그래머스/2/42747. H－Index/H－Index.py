'''
citations를 정렬하여 arr에 저장한다.
arr를 enumerate하여 순회하면서 h의 최댓값을 구한다.
h는 전체 논문 중 현재 논문 이상으로 인용된 논문의 개수(idx)와 현재 논문의 인용 횟수(c) 중 작은 값이다.
'''

def solution(citations):
    arr = sorted(citations, reverse=True)
    answer = 0
    for idx, c in enumerate(arr, start=1):
        answer = max(answer, min(idx, c))
    return answer