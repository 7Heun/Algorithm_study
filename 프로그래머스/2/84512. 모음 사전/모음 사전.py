'''
arr의 카티션 프로덕트를 구해서 모든 가능한 조합을 words에 저장하고 오름차순 정렬한다.
word의 인덱스를 구하고 1을 더한 값을 리턴한다.
'''

from itertools import product

def solution(word):
    arr = ['A', 'E', 'I', 'O', 'U']
    words = []
    for i in range(1, len(arr) + 1):
        for j in product(arr, repeat=i):
            words.append("".join(j))
    words.sort()
    return words.index(word) + 1