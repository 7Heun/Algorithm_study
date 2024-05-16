import sys
input = sys.stdin.readline
dict = {'.':'.', 'O':'O', '-':'|', '|':'-', '/':'\\', '\\':'/', '^':'<', '<':'v', 'v':'>', '>':'^'}
n, m = map(int, input().split())
a = [list(input().strip()) for _ in range(n)]
for i in range(m):
    for j in range(n):
        print(dict[a[j][m-i-1]], end='')
    print()