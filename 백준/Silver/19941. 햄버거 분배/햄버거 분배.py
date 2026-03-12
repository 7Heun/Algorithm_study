import sys
input = sys.stdin.readline

n, k = map(int, input().split())
query = list(input().strip())
ans = 0

for i in range(n):
    if query[i] == 'P':
        s = max(0, i-k)
        e = min(i+k+1, n)

        for j in range(s, e):
            if query[j] == 'H':
                query[j] = 'X'
                ans += 1
                break
print(ans)