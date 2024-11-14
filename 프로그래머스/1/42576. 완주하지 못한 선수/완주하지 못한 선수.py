'''
participant, completion을 정렬한 리스트를 각각 p, c로 두고, 
반복문으로 p, c를 순회하며 비교함.
두 값이 서로 달라지는 시점의 p 값은 c에는 없는 참가자이므로 해당 참가자를 리턴함.
'''

def solution(participant, completion):
    p = sorted(participant)
    c = sorted(completion)
    for i in range(len(c)):
        if p[i] != c[i]:
            return p[i]
    return p[-1]