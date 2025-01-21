'''
수포자들이 찍는 방식을 2차원 배열 arr로 정의하고, answers 배열을 순회하며 정답과 비교한다.
out of index가 발생하지 않도록 모듈러 연산을 활용한다.
정답을 맞추면 score 배열의 요소를 1 증가시킨다.
순회가 끝나면 점수의 최댓값의 인덱스를 차례대로 배열에 저장해 리턴한다.
'''

def solution(answers):
    arr = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    score = [0, 0, 0]
    for i in range(len(answers)):
        for j in range(len(arr)):
            if answers[i] == arr[j][i % len(arr[j])]:
                score[j] += 1
    max_score = max(score)
    return [i + 1 for i, s in enumerate(score) if s == max_score]