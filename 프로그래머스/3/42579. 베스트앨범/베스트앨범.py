'''
장르별로 묶은 후 재생 횟수의 합을 기준으로 내림차순 정렬하고, 원본 인덱스도 함께 저장함.
각 장르에서 재생 횟수가 많고 고유 번호가 낮은 순서로 노래들을 정렬함.
장르별로 정렬된 노래를 최대 2개씩 정답 배열에 추가함.
'''

from collections import defaultdict

def solution(genres, plays):
    arr = defaultdict(list)
    for i in range(len(genres)):
        arr[genres[i]].append((plays[i], i))
    sorted_genre = sorted(arr.keys(), key=lambda x: sum(play[0] for play in arr[x]), reverse=True)
    answer = []
    for genre in sorted_genre:
        arr[genre].sort(key=lambda x: (-x[0], x[1]))
        answer.extend([song[1] for song in arr[genre][:2]])
    return answer
