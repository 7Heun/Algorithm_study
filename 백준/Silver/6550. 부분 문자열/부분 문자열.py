from collections import deque
import sys
input = sys.stdin.readline

while True:
    tmp = input().rstrip()
    if not tmp: break
    s, t = tmp.split()
    t = list(t)
    sq = deque(s)
    string = []
    while sq:
        curr = sq.popleft()
        for j in range(len(t)):
            if t[j] == curr:
                string.append(t[j])
                t = t[j+1:]
                break
    print("Yes" if s == ''.join(string) else "No")
