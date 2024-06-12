num = input().rstrip()
sorted_num = sorted(num, reverse=True)
print(*sorted_num, sep='')