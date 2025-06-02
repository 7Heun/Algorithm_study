def solution(s):
    new_word = True
    answer = ''
    for c in s:
        if c == ' ':
            answer += c
            new_word = True
            continue
        if new_word:
            answer += c.upper()
        else:
            answer += c.lower()
        new_word = False
    return answer