import sys
input = sys.stdin.readline

word = input().strip().upper()
word_set = list(set(word))
word_count = [0] * len(word_set)
for i in range(len(word_set)):
    word_count[i] = word.count(word_set[i])
if word_count.count(max(word_count)) > 1:
    print('?')
else:
    print(word_set[word_count.index(max(word_count))])