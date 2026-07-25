'''
연속 부분 수열에 펄스 수열을 곱했을 때 원소의 합이 최대가 되는 것
수열 전체에 펄스 수열 곱해놓고 원소 합 최대인 부분 수열 추출
dp
-1로 시작하는 펄스 수열, 1로 시작하는 펄스 수열
'''

def solution(sequence):
    plus = []
    minus = []
    flag = 1

    for i in range(len(sequence)):
        plus.append(sequence[i] * flag)
        flag = -flag
        minus.append(sequence[i] * flag)
        
    dp1 = [plus[0]]
    dp2 = [minus[0]]
    for i in range(1, len(sequence)):
        dp1.append(max(plus[i], dp1[i-1] + plus[i]))
        dp2.append(max(minus[i], dp2[i-1] + minus[i]))
    
    return max(max(dp1), max(dp2))
