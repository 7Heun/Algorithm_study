from collections import defaultdict
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    W = input().strip()
    K = int(input())
    pos = defaultdict(list)
    
    for i, c in enumerate(W):
        pos[c].append(i)

    min_len = float('inf')
    max_len = -1

    for p in pos:
        idx_list = pos[p]
        if len(idx_list) < K:
            continue
        for i in range(len(idx_list) - K + 1):
            tmp_len = idx_list[i+K-1] - idx_list[i] + 1
            min_len = min(min_len, tmp_len)
            max_len = max(max_len, tmp_len)
    
    if max_len == -1:
        print(-1)
    else:
        print(min_len, max_len)