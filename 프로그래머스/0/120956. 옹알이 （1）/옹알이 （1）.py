'''
네 가지 발음을 패턴으로 만들고 정규표현식을 이용하여 해당 패턴과 일치하는 부분을 빈 문자열로 치환한다.
모든 과정이 끝났을 때 아예 빈 문자열이 되어있다면 해당 문장은 발음이 가능하므로 그 개수를 세어 리턴한다.
'''

import re
def solution(babbling):
    arr = ["aya", "ye", "woo", "ma"]
    pattern = '|'.join(arr)
    result = [re.sub(pattern, "", b) for b in babbling]
    return result.count("")