'''
arr의 현재 요소와 직접 요소를 비교하여 연속되지 않는 값만 정답 배열에 추가함.
'''

def solution(arr):
    answer = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer