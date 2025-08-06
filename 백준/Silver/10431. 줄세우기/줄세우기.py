import sys
input = sys.stdin.readline

p = int(input())
for _ in range(p):
    arr = list(map(int, input().split()))
    t = arr.pop(0)
    students = []
    ans = 0
    for a in arr:
        idx = 0
        while idx < len(students) and a > students[idx]:
            idx += 1
        ans += len(students) - idx
        students.insert(idx, a)
    print(t, ans)