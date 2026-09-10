'''
최대 입력 개수가 적음
모두 노란불이 되는 때를 리턴
끝까지 탐색해도 겹치는 곳이 없으면 -1 리턴 -> 첫 최소공배수까지만 확인
'''
from math import lcm

def solution(signals):
    n = len(signals)
    # 각 신호를 시간별로 저장
    is_yellows = []
    for g, y, r in signals:
        is_yellows.append([False] * g + [True] * y + [False] * r)
    
    # 최소공배수 시간 구하기
    time = lcm(*(sum(signal) for signal in signals))
    # 현재 시간에 모두 노란불이면 현재 시간 리턴
    for t in range(time):
        if all(is_yellow[t % len(is_yellow)] for is_yellow in is_yellows):
            return t+1
    return -1