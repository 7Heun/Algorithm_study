import sys
input = sys.stdin.readline
while True:
    try:
        n = int(input())
        if n == 1:
            print(1)
            continue
        num = 11
        cnt = 2
        while True:
            if num % n == 0:
                print(cnt)
                break
            num = num * 10 + 1
            cnt += 1
    except:
        break