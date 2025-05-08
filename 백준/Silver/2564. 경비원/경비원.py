import sys
input = sys.stdin.readline
def get_pos(d, x):
    if d == 1:
        return x
    elif d == 2:
        return 2 * w + h - x
    elif d == 3:
        return 2 * (w + h) - x
    elif d == 4:
        return w + x

w, h = map(int, input().split())
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
d, x = map(int, input().split())
donggeun = get_pos(d, x)
total = 2 * (w + h)

ans = 0
for s_d, s_x in arr:
    shop = get_pos(s_d, s_x)
    dist = abs(donggeun - shop)
    ans += min(dist, total - dist)

print(ans)
