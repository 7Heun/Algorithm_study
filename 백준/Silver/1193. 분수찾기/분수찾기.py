import sys
input = sys.stdin.readline 
x = int(input())
n = 1
while n * (n + 1) < 2 * x:
    n += 1
tmp = (n * (n + 1) // 2) - x
print(f"{n - tmp}/{1 + tmp}" if n % 2 == 0 else f"{1 + tmp}/{n - tmp}")