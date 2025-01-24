'''
brown과 yellow를 합친 전체 면적을 area에 저장한다.
a * b = area가 되게 하는 a, b의 값(a >= b)의 리스트로 arr에 저장한다.
리스트를 순회하며 brown, yellow의 조건에 맞는지 검사하고 맞으면 해당 리스트를 리턴한다.
'''

def solution(brown, yellow):
    area = brown + yellow
    arr = []
    for i in range(1, int(area ** 0.5) + 1):
        if area % i == 0:
            arr.append([area // i, i])
    for a in arr:
        if (a[0] * 2 + (a[1] - 2) * 2) == brown and area - brown == yellow:
            return a