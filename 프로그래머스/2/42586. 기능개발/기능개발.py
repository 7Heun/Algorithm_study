'''
progress와 speed를 이용해 작업에 걸리는 날을 계산하여 dates 배열에 저장함.
dates를 순회하며 현재 작업이 앞 작업보다 오래 걸리는 경우 현재까지 쌓인 작업 수(count)를 바로 정답 배열에 저장하고, 그렇지 않으면 count를 1 증가시킴.
순회를 마치면 마지막 카운트를 정답 배열에 저장함.
'''

def solution(progresses, speeds):
    dates = [(100 - p + s - 1) // s for p, s in zip(progresses, speeds)]
    answer = []
    count = 1
    max_day = dates[0]
    for i in range(1, len(dates)):
        if dates[i] > max_day:
            answer.append(count)
            count = 1
            max_day = max(max_day, dates[i])
        else:
            count += 1
    answer.append(count)
    return answer