'''
nums 배열에서 중복을 제거하고,
최대한 다양한 종류의 폰켓몬을 선택하기 위해 N/2와 중복 제거 배열(unique_nums) 중 작은 것을 리턴함
'''

def solution(nums):
    unique_nums = list(set(nums))
    answer = min(len(nums)/2, len(unique_nums))
    return answer