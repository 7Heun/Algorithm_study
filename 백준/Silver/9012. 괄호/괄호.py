import sys

n = int(sys.stdin.readline())

def count(put):
    for j in range (len(put)):
        if put[j] == "(":
            par.append(put[j])
        elif put[j] == ")":
            if len(par) < 1:
                print("NO")
                return
            par.pop()
    if par:
        print("NO")
    else:
        print("YES")
    return

for i in range (n):
    put = []
    par = []
    put = sys.stdin.readline()
    count(put)
    