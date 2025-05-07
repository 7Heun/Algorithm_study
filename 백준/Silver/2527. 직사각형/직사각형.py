import sys
input = sys.stdin.readline
arr = [list(map(int, input().split())) for _ in range(4)]

for a in arr:
    x1, y1, p1, q1, x2, y2, p2, q2 = a

    # 안 겹침
    if p1 < x2 or p2 < x1 or q1 < y2 or q2 < y1:
        print('d')
        continue

    # 점 겹침
    if (p1 == x2 and q1 == y2) or (x1 == p2 and q1 == y2) or \
       (x1 == p2 and y1 == q2) or (p1 == x2 and y1 == q2):
        print('c')
        continue

    # 선분 겹침
    if (p1 == x2 or x1 == p2) and not (q1 <= y2 or q2 <= y1):
        print('b')
        continue
    if (q1 == y2 or y1 == q2) and not (p1 <= x2 or p2 <= x1):
        print('b')
        continue

    # 면적 겹침
    print('a')
