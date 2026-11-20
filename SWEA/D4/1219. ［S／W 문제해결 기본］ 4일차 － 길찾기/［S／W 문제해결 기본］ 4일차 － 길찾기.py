from collections import defaultdict

def check(node, graph, visited):
    stack = [node]
    visited[node] = True

    while stack:
        now = stack.pop()
        if now == 99:
            return 1
        for n in graph[now]:
            if not visited[n]:
                visited[n] = True
                stack.append(n)
    return 0

for test_case in range(10):
    T, N = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = defaultdict(list)
    for i in range(N):
        graph[arr[i*2]].append(arr[i*2+1])
    visited = [False] * 100
    print(f"#{T} {check(0, graph, visited)}")