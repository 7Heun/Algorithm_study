n = int(input())
for i in range(n):
    s = input()
    score = 0
    add = 1
    for i in range(len(s)):
        if s[i] == 'O':
            score += add
            add += 1
        else:
            add = 1
    print(score)