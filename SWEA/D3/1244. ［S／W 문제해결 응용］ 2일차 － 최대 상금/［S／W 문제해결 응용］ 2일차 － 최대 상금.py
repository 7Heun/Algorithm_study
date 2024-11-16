def dfs(n):
    global ans
    if n == count:
        ans = max(ans, int("".join(num_arr)))
        return
    for i in range(l-1):
        for j in range(i+1, l):
            num_arr[i], num_arr[j] = num_arr[j], num_arr[i]
            if (n, int("".join(num_arr))) not in v:
                dfs(n+1)
                v.add((n, int("".join(num_arr))))
            num_arr[i], num_arr[j] = num_arr[j], num_arr[i]

T = int(input())
for test_case in range(1, T + 1):
    num, count = map(int, input().split())
    num_arr = list(str(num))
    l = len(num_arr)
    v = set()
    ans = 0
    dfs(0)
    print(f"#{test_case} {ans}")