import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5+5)

def make_tree(pre_start, pre_end, in_start, in_end):
    if pre_start > pre_end or in_start > in_end:
        return
    
    root = preorder[pre_start]
    root_idx = idx_map[root]
    left_size = root_idx - in_start

    # 왼쪽 서브트리
    make_tree(pre_start+1, pre_start+left_size, in_start, root_idx-1)
    # 오른쪽 서브트리
    make_tree(pre_start+left_size+1, pre_end, root_idx+1, in_end)
    # root
    print(root, end=' ')

t = int(input())
for _ in range(t):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    idx_map = {v: i for i, v in enumerate(inorder)}
    make_tree(0, n-1, 0, n-1)
    print()