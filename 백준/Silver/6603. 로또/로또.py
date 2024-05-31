import sys
input = sys.stdin.readline
print = sys.stdout.write

def dfs(start, cnt, res=[]):
    if cnt == 6:
        print(' '.join(map(str, res)) + '\n')
        return
    for i in range(start, k):
        dfs(i+1, cnt+1, res+[S[i]])

while True:
    k, *S = map(int, input().split())
    if k == 0:
        break
    dfs(0, 0)
    print('\n')