def fibonacci(n):
    if n == 0:
        return 1, 0
    elif n == 1:
        return 0, 1
    else:
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return a, b
        

T = int(input())
for _ in range(T):
    N = int(input())
    print(*fibonacci(N))