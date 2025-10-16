import sys
input = sys.stdin.readline
from collections import defaultdict

def preorder(node):
    if node == '.':
        return
    print(node, end='')
    preorder(graph[node][0])
    preorder(graph[node][1])

def inorder(node):
    if node == '.':
        return
    inorder(graph[node][0])
    print(node, end='')
    inorder(graph[node][1])

def postorder(node):
    if node == '.':
        return
    postorder(graph[node][0])
    postorder(graph[node][1])
    print(node, end='')

n = int(input())
graph = defaultdict(list)
for _ in range(n):
    node, left, right = input().rstrip().split()
    graph[node].append(left)
    graph[node].append(right)

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()