from collections import defaultdict, deque

def bfs(start, graph):
    dq = deque([start])
    visited = [False] * 101
    visited[start] = True
    result = 0

    while dq:
        max_node = 0
        for _ in range(len(dq)):
            now = dq.popleft()
            max_node = max(max_node, now)
            for nxt in graph[now]:
                if not visited[nxt]:
                    visited[nxt] = True
                    dq.append(nxt)
        result = max_node
    return result

for test_case in range(1, 11):
    N, start = map(int, input().split())
    arr = list(map(int, input().split()))

    graph = defaultdict(list)
    for i in range(0, N, 2):
        if arr[i+1] in graph[arr[i]]: continue
        graph[arr[i]].append(arr[i+1])

    print(f"#{test_case} {bfs(start, graph)}")