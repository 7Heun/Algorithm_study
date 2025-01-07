'''
numbers의 각 원소를 문자열로 변환하고 3번 반복한 것을 기준으로 내림차순 정렬한다.
(3번 반복하지 않으면 3, 30 중 30을 큰 것으로 간주하기 때문에 333, 303030으로 변경하여 확실히 정렬되도록 조치하는 것)
정렬된 arr를 문자열로 합치고, 답이 0인 경우를 대비하여 int로 한번 변환한 뒤 다시 문자열로 변환해 리턴한다.
'''

def solution(numbers):
    arr = sorted(map(str, numbers), key=lambda x: x*3, reverse=True)
    return str(int(''.join(arr)))