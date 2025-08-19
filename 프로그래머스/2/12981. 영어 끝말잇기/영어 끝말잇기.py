import math
def solution(n, words):
    used = [words[0]]
    for i in range(1, len(words)):
        now = words[i][0]
        prev = words[i-1][-1]
        # 앞 단어 끝으로 시작하지 않거나 이미 사용한 단어인 경우
        if prev != now or words[i] in used:
            player = (i+1) % n if (i+1) % n else n
            turn = math.ceil((i+1) / n)
            return [player, turn]
        used.append(words[i])
    return [0, 0]