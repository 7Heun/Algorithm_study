import sys
input = sys.stdin.readline

n = int(input())
roads = list(map(int, input().split()))
stations = list(map(int, input().split()))

'''
주유소에 도착한 시점에 남은 이동거리가 있다면, 해당 주유소 가격과 다음 주유소 가격 비교
다음 주유소보다 비싸면 최소 주유, 싸면 다음 싼 주유소가 나올 때까지 이동 가능하게 주유
'''
stations.pop()
total = 0
i = 0
while True:
    if i >= len(stations)-1: break
    if stations[i] > stations[i+1]:
        total += stations[i] * roads[i]
        i += 1
        continue
    next_station = i
    for j in range(i+1, len(stations)):
        if stations[i] > stations[j]:
            next_station = j
            break
        if j == len(stations)-1:
            next_station = len(stations)
    for k in range(i, next_station):
        total += stations[i] * roads[k]
    i = next_station
print(total)