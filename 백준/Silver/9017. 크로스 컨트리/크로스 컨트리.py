from collections import defaultdict
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = defaultdict(int)
    scores = defaultdict(list)
    for a in arr:
        cnt[a] += 1
    i = 1
    for a in arr:
        if cnt[a] == 6:
            scores[a].append(i)
            i += 1
    
    top_score = float('inf')
    top_team = 0
    for team in scores:
        score = sum(scores[team][:4])
        if score < top_score:
            top_score = score
            top_team = team
        elif score == top_score:
            if scores[team][4] < scores[top_team][4]:
                top_score = score
                top_team = team
    print(top_team)
