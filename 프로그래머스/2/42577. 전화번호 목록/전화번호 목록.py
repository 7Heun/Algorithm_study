'''
phone_book을 정렬하고, 효율성을 위해 zip 함수를 이용해 phone_book 배열 두개를 하나로 묶어
startswith 함수로 비교함.
'''

def solution(phone_book):
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True