import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = int(sys.stdin.readline())
e = int(sys.stdin.readline())
score = [a, b, c, d, e]
score_1 = []
for i in score:
    if i < 40 :
        score_1.append(40)
    else:
        score_1.append(i)
ave = int(sum(score_1) / 5)
print(ave)