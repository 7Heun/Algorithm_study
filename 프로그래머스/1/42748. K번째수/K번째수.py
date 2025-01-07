'''
commands를 순회하며 각 조건에 맞추어 array를 자르고 정렬한 배열을 arr에 저장한다.
arr의 k번째에 있는 수를 반환한다.
'''

def solution(array, commands):
    answer = []
    for c in commands:
        arr = sorted(array[c[0]-1:c[1]])
        answer.append(arr[c[2]-1])
    return answer