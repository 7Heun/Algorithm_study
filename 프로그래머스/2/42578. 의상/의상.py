'''
의상을 카테고리별로 묶고, 각 카테고리에서 선택 가능한 수만큼 곱해 조합의 총 개수를 구함.
즉, 각 카테고리별 개수 (n) + 해당 카테고리에서 선택하지 않을 경우 (1) 만큼 곱해감.
마지막에 1을 뺌 (전체 카테고리에서 아무것도 선택하지 않는 경우 고려).
'''

from collections import defaultdict

def solution(clothes):
    category_dict = defaultdict(list)
    for item, category in clothes:
        category_dict[category].append(item)
    answer = 1
    for category, items in category_dict.items():
        answer *= (len(items) + 1)
    answer -= 1
    return answer
    
    