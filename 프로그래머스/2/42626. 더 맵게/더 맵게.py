'''
최소 힙을 이용해 스코빌 지수의 최소값이 K 이상이 될 때까지 주어진 조건에 맞게 스코빌 지수를 업데이트한다.
만약 가능한 만큼 업데이트가 끝났는데 스코빌 지수의 최소값이 K 이상이 되지 않으면 -1을 리턴한다.
'''

import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
        answer += 1
    return answer