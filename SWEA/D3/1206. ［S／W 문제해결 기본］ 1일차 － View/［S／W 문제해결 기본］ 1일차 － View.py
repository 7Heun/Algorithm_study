T = 10
for test_case in range(1, T + 1):
	n = int(input())
	buildings = list(map(int, input().split()))
	ans = 0
	for i in range(2, n-2):
		maxHeight = max(buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2])
		if buildings[i] > maxHeight:
			ans += (buildings[i] - maxHeight)
	print(f"#{test_case} {ans}")