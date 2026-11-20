T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_price = 0
    ans = 0

    for price in reversed(arr):
        if price > max_price:
            max_price = price
        else:
            ans += max_price - price

    print(f"#{test_case} {ans}")