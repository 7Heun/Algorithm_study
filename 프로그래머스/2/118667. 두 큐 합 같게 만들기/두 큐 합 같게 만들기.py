from collections import deque
def solution(queue1, queue2):
    sum1, sum2 = sum(queue1), sum(queue2)
    target = sum1 + sum2
    if target % 2 == 1: return -1
    target //= 2
    
    dq1, dq2 = deque(queue1), deque(queue2)
    count = 0
    limit = len(queue1) + len(queue2)
    
    while sum1 != sum2:
        if count >= limit: return -1
        while dq1 and sum1 > sum2:
            tmp = dq1.popleft()
            dq2.append(tmp)
            sum1 -= tmp
            sum2 += tmp
            count += 1
        while dq2 and sum2 > sum1:
            tmp = dq2.popleft()
            dq1.append(tmp)
            sum2 -= tmp
            sum1 += tmp
            count += 1
    return count