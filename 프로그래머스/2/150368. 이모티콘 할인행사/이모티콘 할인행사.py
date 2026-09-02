'''
[플러스 가입 수, 매출액]
사용자별로 할인 비율과 가격 따짐
cartesian product
'''
from itertools import product

def solution(users, emoticons):
    per = [10, 20, 30, 40]
    m = len(emoticons)
    # 발생할 수 있는 모든 할인율 조합 체크
    discount_rates = list(product(per, repeat=m))
    
    # 할인율 조합별로 최적 답 찾아서 저장
    res = []
    for discount_rate in discount_rates:
        member = 0  # 이모티콘 플러스 가입자 수
        total = 0   # 이모티콘 판매액
        
        # 유저별로 순회
        for rate, budget in users:
            user_total = 0
            # 각 이모티콘 별로 할인율이 유저의 기준 이상인 것만 체크
            for i in range(m):
                if discount_rate[i] >= rate:
                    # 이모티콘 구입
                    user_total += emoticons[i] * (100 - discount_rate[i]) // 100
                    # 이모티콘 플러스 가입 기준 되면 구매 모두 취소 후 플러스 가입
                    if user_total >= budget:
                        member += 1
                        user_total = 0
                        break
            # 이모티콘 플러스 가입 안 했으면 전체 판매액에 가산
            total += user_total
        # 이번 조합으로 얻을 수 있는 결과 저장
        res.append((member, total))
    # 이모티콘 플러스 가입자 > 이모티콘 판매액 최적 답 리턴
    sorted_res = sorted(res, key=lambda x: (x[0], x[1]), reverse=True)
    return sorted_res[0]        
        