'''
경로를 오름차순 정렬하고, 기준점(카메라 위치)을 첫번째 경로의 진출 지점으로 설정한다.
route를 순회하며 기준점과 현재 경로의 진입 지점을 비교한다.
만약 현재 경로의 진입 지점이 기준점보다 크면 겹치는 지점이 없다는 것이므로 새 카메라를 설치한다(기준점을 현재 경로의 진출 지점으로 업데이트, answer 1 증가).
그렇지 않으면 겹치는 지점이 있어 현재 카메라를 만날 수 있다는 뜻이므로 기준점만 업데이트한다(기준점과 현재 경로의 진출 지점 중 더 작은 값으로).
'''

def solution(routes):
    routes.sort()
    standard = routes[0][1]
    answer = 1
    for route in routes[1:]:
        if route[0] > standard:
            standard = route[1]
            answer += 1
        else:
            standard = min(route[1], standard)
    return answer