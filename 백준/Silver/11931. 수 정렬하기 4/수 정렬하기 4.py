import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort(reverse=True)
for i in arr:
    print(str(i) + '\n')