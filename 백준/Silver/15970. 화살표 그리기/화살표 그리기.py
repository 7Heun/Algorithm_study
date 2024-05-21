import sys
input = sys.stdin.readline
n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
total_distance = 0
points.sort(key=lambda x: (x[1], x[0]))
for i in range(n):
    distance_left = distance_right = 9912341234
    if i == 0:
        total_distance += abs(points[i+1][0] - points[i][0])
        continue
    if i == n-1:
        total_distance += abs(points[i][0] - points[i-1][0])
        continue
    if points[i][1] == points[i-1][1]:
        distance_left = abs(points[i][0] - points[i-1][0])
    if points[i][1] == points[i+1][1]:
        distance_right = abs(points[i][0] - points[i+1][0])
    total_distance += min(distance_left, distance_right)
print(total_distance)