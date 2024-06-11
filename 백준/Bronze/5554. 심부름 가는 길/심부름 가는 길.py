arr = []
for _ in range(4):
    arr.append(int(input()))
total = sum(arr)
print(total // 60)
print(total % 60)