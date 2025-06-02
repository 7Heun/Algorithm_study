from collections import defaultdict
def solution(id_list, report, k):
    arr = defaultdict(list)
    count = defaultdict(int)
    banned = set()
    for r in report:
        a, b = r.split()
        if b in arr[a]: continue
        arr[a].append(b)
        count[b] += 1
        if count[b] >= k:
            banned.add(b)
    answer = []
    for id in id_list:
        if id not in arr:
            answer.append(0)
            continue
        tmp = set(arr[id])
        tmp = tmp.intersection(banned)
        answer.append(len(tmp))
    return answer        