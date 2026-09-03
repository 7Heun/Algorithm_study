'''
집합을 먼저 나눠야 함 {} 기준으로
집합들을 원소 개수로 sort
리스트 하나 만들고 다음 집합에서 새로 등장한 숫자 append
'''

def solution(s):
    # 주어진 집합 문자열을 리스트로 만드는 작업
    new_s = []
    tmp = s.lstrip('{').rstrip('}').split('},{')
    lst = [list(map(int, t.split(','))) for t in tmp]
    sorted_lst = sorted(lst, key=len)
    ans = sorted_lst[0]
    
    # 다음 집합에서 현재 집합에 없는 숫자 찾아서 append
    for i in range(1, len(sorted_lst)):
        for n in sorted_lst[i]:
            if n not in sorted_lst[i-1]:
                ans.append(int(n))
    return ans