import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

min_n = 1000000001
max_n = -1000000001

def dfs(idx, total, plus, minus, mul, div):
    global min_n, max_n
    if idx == N:
        min_n = min(min_n, total)
        max_n = max(max_n, total)
        return
    if plus:
        dfs(idx+1, total + arr[idx], plus-1, minus, mul, div)
    if minus:
        dfs(idx+1, total - arr[idx], plus, minus-1, mul, div)
    if mul:
        dfs(idx+1, total * arr[idx], plus, minus, mul-1, div)
    if div:
        if total < 0:
            dfs(idx+1, -(-total // arr[idx]), plus, minus, mul, div-1)
        else:
            dfs(idx+1, total // arr[idx], plus, minus, mul, div-1)

dfs(1, arr[0], plus, minus, mul, div)
print(max_n)
print(min_n)