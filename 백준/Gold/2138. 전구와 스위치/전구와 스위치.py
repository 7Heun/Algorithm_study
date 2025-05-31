import sys
input = sys.stdin.readline

N = int(input())
bulbs = list(map(int, input().strip()))
target = list(map(int, input().strip()))

def toggle(switch, idx):
    for i in range(idx-1, idx+2):
        if 0 <= i < N:
            switch[i] ^= 1

def count(bulbs, toggle_first):
    bulbs_copy = bulbs[:]
    cnt = 0
    if toggle_first:
        toggle(bulbs_copy, 0)
        cnt += 1

    for i in range(1, N):
        if bulbs_copy[i-1] != target[i-1]:
            toggle(bulbs_copy, i)
            cnt += 1
    return cnt if bulbs_copy == target else float('inf')

res = min(count(bulbs, False), count(bulbs, True))
print(res if res != float('inf') else -1)