import sys
input = sys.stdin.readline

n = int(input())
roads = list(map(int, input().split()))
stations = list(map(int, input().split()))

# 현재 주유소에서 지금까지 본 것 중 가장 싼 가격으로 다음 도시까지 주유
min_price = stations[0]
total = 0

for i in range(n-1):
    if stations[i] < min_price:
        min_price = stations[i]
    total += min_price * roads[i]
print(total)