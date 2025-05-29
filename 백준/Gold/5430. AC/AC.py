from collections import deque
import sys
input = sys.stdin.readline

def run_p(p, arr):
    r_cnt = 0
    for func in p:
        if func == 'R':
            r_cnt += 1
            continue
        else:
            if r_cnt % 2 == 1:
                tmp = arr.pop()
            else:
                tmp = arr.popleft()
    if r_cnt % 2 == 1:
        arr.reverse()
    return arr

T = int(input())
for _ in range(T):
    p = input().strip()
    n = int(input())
    tmp = input().strip().removeprefix('[').removesuffix(']')
    if n == 0:
        arr = deque([])
    else:
        arr = deque(map(int, tmp.split(",")))
    if p.count("D") > n:
        print("error")
        continue
    arr = run_p(p, arr)
    strarr = [str(a) for a in arr]
    print("[" + ",".join(strarr) + "]")
