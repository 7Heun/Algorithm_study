import sys
input = sys.stdin.readline

w, h = map(int, input().split())
n = int(input())
horizontal = [0, h]
vertical = [0, w]

for _ in range(n):
    di, pos = map(int, input().split())
    if di == 0:
        horizontal.append(pos)
    else:
        vertical.append(pos)

horizontal.sort()
vertical.sort()

height = []
width = []
for i in range(1, len(horizontal)):
    height.append(horizontal[i] - horizontal[i-1])
for i in range(1, len(vertical)):
    width.append(vertical[i] - vertical[i-1])

ans = 0
for he in height:
    for wi in width:
        ans = max(ans, he * wi)

print(ans)