import itertools
import sys       
input = sys.stdin.readline
N = int(input())
arr = [i for i in range(1, N+1)]
for perm in itertools.permutations(arr):
    print(*perm)