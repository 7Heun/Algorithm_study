def solution(friends, gifts):
    arr = [[0] * len(friends) for _ in range(len(friends))]
    score = [0] * len(friends)
    next_month = [0] * len(friends)
    for g in gifts:
        s, r = g.split()
        arr[friends.index(s)][friends.index(r)] += 1
        score[friends.index(s)] += 1
        score[friends.index(r)] -= 1
    for r in range(len(friends)):
        for c in range(len(friends)):
            if r == c: continue
            if arr[r][c] > arr[c][r]:
                next_month[r] += 1
            if arr[r][c] == arr[c][r]:
                if score[r] > score[c]:
                    next_month[r] += 1
    return max(next_month)
    
    