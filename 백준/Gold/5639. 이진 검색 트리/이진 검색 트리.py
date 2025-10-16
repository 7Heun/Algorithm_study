import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5+5)

preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break

def postorder(start, end):
    if start > end:
        return
    root = preorder[start]
    i = start + 1
    while i <= end and preorder[i] < root:
        i += 1
    # 왼쪽 서브트리
    postorder(start+1, i-1)
    # 오른쪽 서브트리
    postorder(i, end)
    # 루트
    print(root)

postorder(0, len(preorder)-1)