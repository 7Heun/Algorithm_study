import sys
import math
input = sys.stdin.readline
k = int(input())
max_range = int(k * math.log(k) * 1.2)
prime = [True] * max_range
prime[0] = prime[1] = False
count = 0
for i in range(2, max_range):
    if prime[i]:
        count += 1
        if count == k:
            print(i)
            break
        for j in range(i*2, max_range, i):
            prime[j] = False