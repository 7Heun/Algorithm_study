'''
명함들을 가로/세로 비율이 비슷하도록 적절히 회전시킨다. (2차원 배열 속 리스트 정렬)
가로/세로에서 각각 최댓값을 찾아 곱한 값을 리턴한다.
'''

def solution(sizes):
    for lst in sizes:
        lst.sort()
    w = max(s[0] for s in sizes)
    h = max(s[1] for s in sizes)
    return w * h
    