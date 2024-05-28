import sys
input = sys.stdin.readline
ans = []
while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    num = [a, b, c]
    num.sort()
    if num[0] ** 2 + num[1] ** 2 == num[2] ** 2:
        ans.append('right')
    else:
        ans.append('wrong')
print('\n'.join(ans))