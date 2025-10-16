import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5+5)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

idx_map = {value: i for i, value in enumerate(inorder)}

def make_tree(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return
    # 루트
    root = postorder[post_end]
    print(root, end=' ')

    root_idx = idx_map[root]
    left_size = root_idx - in_start

    # 왼쪽 서브트리
    make_tree(in_start, root_idx-1, post_start, post_start+left_size-1)
    # 오른쪽 서브트리
    make_tree(root_idx+1, in_end, post_start+left_size, post_end-1)

make_tree(0, n-1, 0, n-1)