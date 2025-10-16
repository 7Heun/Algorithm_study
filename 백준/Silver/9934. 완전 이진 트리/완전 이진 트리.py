import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5+5)
from collections import defaultdict

# input: inorder
k = int(input())
inorder = list(map(int, input().split()))
levels = defaultdict(list)

def make_tree(level, left, right):
    if left > right:
        return
    mid = (left + right) // 2
    levels[level].append(inorder[mid])
    make_tree(level+1, left, mid-1)
    make_tree(level+1, mid+1, right)

make_tree(0, 0, len(inorder)-1)
for level in levels:
    print(*levels[level])