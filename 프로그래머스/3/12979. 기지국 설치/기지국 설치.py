def solution(n, stations, w):
    answer = 0
    coverage = 2 * w + 1

    # 왼쪽 빈 구간
    right = stations[0] - w - 1
    if right >= 1:
        answer += (right + coverage - 1) // coverage

    # 중간 빈 구간
    for i in range(len(stations) - 1):
        left = stations[i] + w + 1
        right = stations[i + 1] - w - 1
        if left <= right:
            remain = right - left + 1
            answer += (remain + coverage - 1) // coverage

    # 오른쪽 빈 구간
    left = stations[-1] + w + 1
    if left <= n:
        remain = n - left + 1
        answer += (remain + coverage - 1) // coverage

    return answer