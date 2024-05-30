max = 1000000

M = [0 for i in range(max+1)]
m = [0 for i in range(max+1)]

for i in range(1,max+1):
    j = 1
    while i * j <= max:
        m[i*j] += i
        j += 1
    M[i] = M[i-1] + m[i]

T = int(input())
arr = list()
for i in range(T):
    arr.append(int(input()))
for i in arr:
    print(M[i])