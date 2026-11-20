for test_case in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(N):
        if max(arr) - min(arr) <= 1: break
        arr[arr.index(max(arr))] -= 1
        arr[arr.index(min(arr))] += 1

    ans = max(arr) - min(arr)
    print(f"#{test_case} {ans}")