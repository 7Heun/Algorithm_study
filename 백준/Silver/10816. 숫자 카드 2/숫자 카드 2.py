import sys
input = sys.stdin.readline
N = int(input())
cards = list(map(int, input().split()))
M = int(input())
queries = list(map(int, input().split()))

cnt = {}
for card in cards:
    if card in cnt:
        cnt[card] += 1
    else:
        cnt[card] = 1

for query in queries:
    if query in cnt:
        print(cnt[query], end=' ')
    else:
        print(0, end=' ')