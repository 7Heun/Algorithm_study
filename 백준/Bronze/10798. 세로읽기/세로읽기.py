words = [input() for i in range(5)]
max_len = 0
for i in range(15):
    for word in words:
        if i < len(word):
            print(word[i], end='')