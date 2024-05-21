import sys
input = sys.stdin.readline
k = int(input())
prime = [2]
num = 3
while len(prime) < k:
    for i in prime:
        if i**2 > num:
            prime.append(num)
            break
        if num % i == 0:
            break
    num += 2
print(prime[-1])