'''
priorities의 원소와 인덱스를 묶어 데크로 만든다.
왼쪽에서부터 pop하여 데크에 현재 프로세스보다 우선순위가 높은 프로세스가 남아있으면 다시 append한다.
만약 그런 프로세스가 없으면 cnt를 1 증가시키고, 인덱스가 location과 같으면 cnt를 리턴한다.
'''

from collections import deque

def solution(priorities, location):
    q = deque(enumerate(priorities))
    cnt = 0
    while q:
        idx, p = q.popleft()
        if any(p < tmp for _, tmp in q):
            q.append([idx, p])
            continue
        cnt += 1
        if idx == location:
            return cnt