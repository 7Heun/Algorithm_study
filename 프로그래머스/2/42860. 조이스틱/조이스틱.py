'''
조이스틱을 상하로 움직이는 것은 최적화가 필요하지 않으므로 단순히 상/하 중 최소 움직임을 answer에 더한다.
좌우로 움직이는 경우를 비교하기 위해 좌/우 각각 얼마나 움직여야 A가 아닌 글자가 나오는지 세고, 최소 움직임을 찾아 answer에 더한다.
이때, A가 연속으로 나오는 지점을 피해 오른쪽으로 끝까지 가는 경우와 왼쪽으로 갔다가 돌아오는 경우 중 최소 움직임을 찾아 answer에 더하는 방식을 사용한다.
'''

def solution(name):
    answer = sum(min(ord(c) - ord('A'), ord('Z') - ord(c) + 1) for c in name)
    min_move = len(name) - 1
    for i in range(len(name)):
        next_idx = i + 1
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1
        min_move = min(min_move, i + len(name) - next_idx + min(i, len(name) - next_idx))
    answer += min_move
    return answer