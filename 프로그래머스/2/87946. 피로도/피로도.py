'''
permutations를 이용해 가능한 모든 순열들을 만들고, 문제에서 제시된 조건을 점검한다.
조건에 부합하면 answer의 최댓값을 갱신한다.
'''

from itertools import permutations

def is_possible_to_explore(k, arr):
    tiredness = k
    for a in arr:
        if tiredness < a[0]:
            return False
        tiredness -= a[1]
    return True

def solution(k, dungeons):
    answer = 0
    for i in range(1, len(dungeons) + 1):
        for j in permutations(dungeons, i):
            if is_possible_to_explore(k, j):
                answer = max(len(j), answer)
    return answer