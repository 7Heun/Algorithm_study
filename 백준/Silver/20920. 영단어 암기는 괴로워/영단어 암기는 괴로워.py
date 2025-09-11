from collections import defaultdict
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
words = defaultdict(int)
for _ in range(n):
    word = input().rstrip()
    if len(word) >= m:
        words[word] += 1

sorted_words = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for word, _ in sorted_words:
    print(word)
