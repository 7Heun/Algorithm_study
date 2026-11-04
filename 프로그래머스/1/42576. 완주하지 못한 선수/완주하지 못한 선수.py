from collections import Counter
def solution(participant, completion):
    p = Counter(participant)
    c = Counter(completion)
    ans = list((p - c).keys())
    return ans[0]
    