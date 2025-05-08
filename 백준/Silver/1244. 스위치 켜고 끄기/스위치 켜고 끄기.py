import sys
input = sys.stdin.readline
n = int(input())
switches = list(map(int, input().split()))
student = int(input())
for _ in range(student):
    sex, num = map(int, input().split())
    if sex == 1:
        for i in range(len(switches)):
            if (i+1) % num == 0:
                switches[i] = 0 if switches[i] else 1
    else:
        num -= 1
        left, right = num-1, num+1
        switches[num] = 0 if switches[num] else 1
        while left >= 0 and right < len(switches):
            if switches[left] != switches[right]:
                break
            switches[left] = 0 if switches[left] else 1
            switches[right] = 0 if switches[right] else 1
            left -= 1
            right += 1
            
for i in range(len(switches)):
    print(switches[i], end=' ')
    if (i + 1) % 20 == 0:
        print()
