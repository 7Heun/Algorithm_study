N = int(input())

for i in range(1, N + 1):
    cnt = sum(c in '369' for c in str(i))
    print('-' * cnt if cnt else i, end=' ')