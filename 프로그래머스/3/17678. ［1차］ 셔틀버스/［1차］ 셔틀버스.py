'''
9:00 첫 차
n: 셔틀 운행 횟수, t: 셔틀 운행 간격(분), m: 한 셔틀 최대 크루 수
콘은 막차 인원이 m보다 많을 때 m번째 도착한 크루보다 1분 일찍 도착해야 함
만약 막차 인원이 m 이하면 막차 타면 됨
'''

def solution(n, t, m, timetable):
    # timetable 분으로 변환
    min_table = []
    for ts in timetable:
        tmp = int(ts[:2]) * 60 + int(ts[3:])
        min_table.append(tmp)
    # 내림차순 정렬 (늦게 도착한 순서대로)
    min_table.sort(reverse=True)

    curr = 9 * 60

    # 막차 전까지 pop으로 일찍 도착한 크루부터 빼기
    for i in range(n):
        boarded = 0
        last_time = 0
        # 자리가 남았고, 대기열이 있고, 대기자 도착 시간이 현재 셔틀 시간 이전이면 pop
        while boarded < m and min_table and min_table[-1] <= curr:
            last_time = min_table.pop()
            boarded += 1
        
        # 막차 처리
        if i == n-1:
            # 막차가 꽉 차는 경우 마지막 도착 사람보다 1분 일찍 도착
            if boarded == m:
                ans = last_time - 1
            # 막차 탈 수 있으면 현재 셔틀 타기
            else:
                ans = curr
        curr += t

    return f"{ans//60:02d}:{ans%60:02d}"
   