import sys
input = sys.stdin.readline
N = int(input())
card = list(map(int, input().split()))
M = int(input())
req = list(map(int, input().split()))
card.sort()
for r in req:
    start, end = 0, N-1
    while start <= end:
        mid = (start + end) // 2
        if r == card[mid]:
            print(1, end=' ')
            break
        elif r < card[mid]:
            end = mid - 1
        else:
            start = mid + 1
    else:
        print(0, end=' ')