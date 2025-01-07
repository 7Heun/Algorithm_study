'''
대기 트럭(q)이나 다리를 건너는 트럭(curr_bridge) 모두 비어 있게 될 때까지 반복한다.
먼저 전체 경과 시간을 나타내는 answer를 1 증가시킨다.
만약 다리를 건너는 트럭이 있다면 다리에 있는 각 트럭의 경과 시간을 1 증가시키고,
맨 앞 트럭이 다리를 다 건넜다면(경과 시간이 bridge_length와 같다면) curr_bridge에서 제거한다.
만약 대기 트럭이 있다면 bridge_length와 weight를 참고해 첫번째 대기 트럭(q[0])이 다리에 올라갈 수 있는지 판단한다.
만약 다리에 올라갈 수 있으면 curr_bridge에 트럭과 경과 시간(1초)을 묶어 추가하고, q에서 제거한다.
'''

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque(truck_weights)
    curr_bridge = deque()
    while q or curr_bridge:
        answer += 1
        if curr_bridge:
            for i in range(len(curr_bridge)):
                curr_bridge[i] = (curr_bridge[i][0], curr_bridge[i][1] + 1)
            if curr_bridge[0][1] > bridge_length:
                curr_bridge.popleft()
        if q:
            curr_truck = q[0]
            if len(curr_bridge)+1 <= bridge_length and sum(truck[0] for truck in curr_bridge) + curr_truck <= weight:
                q.popleft()
                curr_bridge.append((curr_truck, 1))
    return answer