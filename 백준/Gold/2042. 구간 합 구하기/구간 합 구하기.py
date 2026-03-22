import sys
input = sys.stdin.readline

'''
세그트리
1 -> 업데이트
2 -> 구간 합 출력
'''

def build(node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        build(node*2, start, mid)
        build(node*2+1, mid+1, end)
        tree[node] = tree[node*2] + tree[node*2+1]

def update(node, start, end, idx, new):
    if idx < start or end < idx: return
    if start == end:
        tree[node] = new
        return
    mid = (start + end) // 2
    update(node*2, start, mid, idx, new)
    update(node*2+1, mid+1, end, idx, new)
    tree[node] = tree[node*2] + tree[node*2+1]

def total(node, start, end, left, right):
    if right < start or end < left: return 0
    # 구간에 포함
    if left <= start and end <= right:
        return tree[node]
    # 걸침
    mid = (start + end) // 2
    return total(node*2, start, mid, left, right) + total(node*2+1, mid+1, end, left, right)


n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
tree = [0] * (n * 4)
build(1, 0, n-1)

for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, 0, n-1, b-1, c)
    else:
        print(total(1, 0, n-1, b-1, c-1))