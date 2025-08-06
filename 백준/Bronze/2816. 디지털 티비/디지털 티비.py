import sys
input = sys.stdin.readline

n = int(input())
arr = [input().strip() for _ in range(n)]
ans = ""
idx1 = arr.index("KBS1")
ans += '1' * idx1 + '4' * idx1
idx2 = arr.index("KBS2")
if idx2 > idx1:
    idx2 -= 1
ans += '1' * (idx2+1) + '4' * idx2
print(ans)