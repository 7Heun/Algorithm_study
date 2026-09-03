'''
집합을 먼저 나눠야 함 {} 기준으로
집합들을 원소 개수로 sort
리스트 하나 만들고 다음 집합에서 새로 등장한 숫자 append
'''

def solution(s):
    # 주어진 집합 문자열을 리스트로 만드는 작업
    new_s = []
    s = s[1:-2].split('},')
    for a in s:
        if a[0] == '{':
            new_s.append(list(map(int, a[1:].split(','))))
        else:
            new_s.append(list(map(int, a.split(','))))
    sorted_s = sorted(new_s, key=lambda x: len(x))
    ans = sorted_s[0]
    
    # 다음 집합에서 현재 집합에 없는 숫자 찾아서 append
    for i in range(1, len(sorted_s)):
        for n in sorted_s[i]:
            if n not in sorted_s[i-1]:
                ans.append(int(n))
    return ans