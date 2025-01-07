'''
prices의 왼쪽부터 순회하여,
남은 가격 중 현재 가격보다 낮은 가격이 나오면 가격이 떨어졌음을 의미하므로
그때까지를 카운트하여 answer에 저장한다.
'''

from collections import deque

def solution(prices):
    answer = []
    q = deque(prices)
    while q:
        now = q.popleft()
        cnt = 0
        for n in q:
            cnt += 1
            if now > n: break
        answer.append(cnt)
    return answer