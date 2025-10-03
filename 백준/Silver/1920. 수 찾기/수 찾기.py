import sys
input = sys.stdin.readline

n = int(input())
arr = set(map(int, input().split()))    # 해시 탐색
m = int(input())
brr = list(map(int, input().split()))

for b in brr:
    print(1 if b in arr else 0)