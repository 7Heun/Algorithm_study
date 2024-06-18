import sys
input = sys.stdin.readline 
a, b = input().split()
b = int(b)
a_len = len(str(a).split('.')[1])
a = int(a.replace('.', ''))
tmp = str(a ** b)
if len(tmp) <= a_len * b:
    print('0.' + '0' * (a_len * b - len(tmp)) + tmp)
else:
    print(tmp[:-a_len * b] + '.' + tmp[-a_len * b:])