T = int(input())
for _ in range(T):
    N = int(input())
    Li = list(map(int, input().split()))
    Li.sort()
    max_diff = 0
    for i in range(2, N):
        max_diff = max(max_diff, abs(Li[i] - Li[i-2]))
    print(max_diff)