import sys
input = sys.stdin.readline
n = int(input())
cnt = 0
for i in range(1, n+1):
    if i < 100:
        cnt += 1
        continue
    nums = list(map(int, str(i)))
    if nums[1] - nums[0] == nums[2] - nums[1]:
        cnt += 1
        continue
print(cnt)