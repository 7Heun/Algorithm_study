import sys
input = sys.stdin.readline

for _ in range(3):
    arr = list(map(int, input().split()))
    back = arr.count(1)
    if back == 3:
        print("A")
    elif back == 2:
        print("B")
    elif back == 1:
        print("C")
    elif back == 0:
        print("D")
    else:
        print("E")