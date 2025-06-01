import heapq
def solution(operations):
    hq = []
    heapq.heapify(hq)
    for op in operations:
        o, n = op.split()
        n = int(n)
        if o == 'I':
            heapq.heappush(hq, n)
            continue
        if not hq: continue
        if n == 1:
            hq.remove(max(hq))
        elif n == -1:
            heapq.heappop(hq)
    if not hq:
        return [0, 0]
    return [max(hq), min(hq)]
            