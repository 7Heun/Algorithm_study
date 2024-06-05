import sys
import re
input = sys.stdin.readline
compare = re.compile('^[A-F]?A+F+C+[A-F]?$')

for _ in range(int(input())):
    s = input().rstrip()
    print("Infected!") if compare.match(s) else print("Good")