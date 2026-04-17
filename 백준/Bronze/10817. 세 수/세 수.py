a, b, c = map(int,input().split())
d = [a, b, c]
d.remove(min(d))
d.remove(max(d))
print(d[0])