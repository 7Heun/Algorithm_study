'''
lost, reserve에서 중복을 제거하여 여벌 옷을 챙긴 학생이 도난당한 경우를 처리하고, 오름차순 정렬한다.
lost의 복사본을 만들어 arr로 저장한다.
lost의 요소를 순회하며 각 요소의 바로 앞번호나 바로 뒷번호 학생이 reserve에 있는지 점검한다.
만약 있으면, reserve와 arr에서 각각 해당하는 요소를 삭제한다.
순회가 끝나면 전체 학생 수에서 arr에 있는 학생 수를 빼서 리턴한다.
'''

def solution(n, lost, reserve):
    lost_set = set(lost)
    reserve_set = set(reserve)
    common_set = lost_set & reserve_set
    lost = list(lost_set - common_set)
    reserve = list(reserve_set - common_set)
    lost.sort()
    reserve.sort()
    arr = lost.copy()
    for l in lost:
        a = l - 1
        b = l + 1
        if a in reserve or b in reserve:
            arr.remove(l)
            reserve.remove(a if a in reserve else b)
    return n - len(arr)