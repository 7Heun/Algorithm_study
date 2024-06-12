T = int(input())
for _ in range(T):
    C = int(input())
    q, d, n, p = 0, 0, 0, 0
    while C > 0:
        if C >= 25:
            q = C // 25
            C %= 25
        elif C >= 10:
            d = C // 10
            C %= 10
        elif C >= 5:
            n = C // 5
            C %= 5
        else:
            p = C
            C = 0
    print(q, d, n, p)