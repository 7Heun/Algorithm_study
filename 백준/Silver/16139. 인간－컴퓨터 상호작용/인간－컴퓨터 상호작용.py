import sys
input = sys.stdin.readline

s = input().strip()
q = int(input())
arr = [[0] * (len(s) + 1) for _ in range(26)]

for i in range(len(s)):
    c = ord(s[i]) - ord('a')
    for j in range(26):
        arr[j][i+1] = arr[j][i] + (1 if j == c else 0)

for _ in range(q):
    a, l, r = input().split()
    l, r = int(l), int(r)
    i = ord(a) - ord('a')
    print(arr[i][r+1] - arr[i][l])