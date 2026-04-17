import sys
input = sys.stdin.readline

arr = list(input())
stick = []
ans = 0
prev = None

for i in range(len(arr)):
    if arr[i] == '(':
        stick.append(arr[i])
    elif arr[i] == ')':
        if prev == '(':
            stick.pop()
            ans += len(stick)
        elif prev == ')':
            ans += 1
            stick.pop()
    prev = arr[i]
print(ans)
