import sys
input = sys.stdin.readline

n, x = map(int, input().split())
visitors = list(map(int, input().split()))

def solution():
    if not sum(visitors):
        print("SAD")
        return
    # 슬라이딩 윈도우
    total = sum(visitors[:x])
    max_total = total
    cnt = 1
    for i in range(1, n-x+1):
        total = total - visitors[i-1] + visitors[i+x-1]
        if total > max_total:
            max_total = total
            cnt = 1
        elif total == max_total:
            cnt += 1
    print(max_total)
    print(cnt)

solution()
