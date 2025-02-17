'''
투 포인터를 사용해 문제를 해결한다.
people을 몸무게 순으로 정렬한다.
people을 순회하며 현 시점 가장 가벼운 사람과 가장 무거운 사람의 몸무게 합이 limit 이하이면 둘 다 보트에 태우고(start, end 포인터 변경, answer 1 증가), 그렇지 않으면 가장 무거운 사람만 태운다(end 포인터 변경, answer 1 증가).
'''

def solution(people, limit):
    answer = 0
    people.sort()
    start, end = 0, len(people) - 1
    while start <= end:
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1
        answer += 1
    return answer