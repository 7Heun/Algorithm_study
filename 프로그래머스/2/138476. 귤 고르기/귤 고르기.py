'''
귤 종류별로 카운트, 내림차순 정렬
반복문 돌면서 k개 채워질 때 i 리턴
'''
from collections import Counter
def solution(k, tangerine):
    c = Counter(tangerine)
    cnt = c.most_common()
    for i, (n, v) in enumerate(cnt):
        k -= v
        if k <= 0: return i+1