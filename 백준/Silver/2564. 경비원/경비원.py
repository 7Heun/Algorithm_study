import sys
input = sys.stdin.readline
w, h = map(int, input().split())
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dire_x, dist_x = map(int, input().split())
ans = 0
for a in arr:
    dire_a, dist_a = a
    if dire_a == dire_x:
        ans += abs(dist_a - dist_x)
        continue
    if dire_a + dire_x == 3:    # 맞은편 (북, 남)
        d1 = dist_x + dist_a + h
        d2 = w * 2 - dist_x - dist_a + h
        ans += min(d1, d2)
        continue
    if dire_a + dire_x == 7:    # 맞은편 (서, 동)
        d1 = dist_x + dist_a + w
        d2 = h * 2 - dist_x - dist_a + w
        ans += min(d1, d2)
        continue
    if dire_a + dire_x == 4:    # 북, 서
        ans += dist_x + dist_a
        continue
    if dire_a + dire_x == 6:    # 남, 동
        if dire_x == 2:
            ans += w - dist_x + h - dist_a
        else:
            ans += h - dist_x + w - dist_x
        continue
    if dire_x == 1: # 동근 북, 상점 동
        ans += w - dist_x + dist_a
    elif dire_x == 4:   # 동근 동, 상점 북
        ans += w - dist_a + dist_x
    elif dire_x == 2:   # 동근 남, 상점 서
        ans += dist_x + h - dist_a
    elif dire_x == 3:   # 동근 서, 상점 남
        ans += dist_a + h - dist_x
print(ans)