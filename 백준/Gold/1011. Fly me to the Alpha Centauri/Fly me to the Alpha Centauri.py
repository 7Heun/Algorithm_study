T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    distance = y - x
    n = 0
    while True:
        if n * (n+1) >= distance:
            break
        n += 1
    if distance > n**2:
        print(2*n)
    else:
        print(2*n-1)