'''
lcm = gcm * a' * b' 활용
'''
def get_lcm(a, b):
    gcm = 1
    for i in range(2, min(a, b)+1):
        while a % i == 0 and b % i == 0:
            a //= i
            b //= i
            gcm *= i
    return gcm * a * b

def solution(arr):
    lcm = arr[0]
    for i in range(1, len(arr)):
        lcm = get_lcm(lcm, arr[i])
    return lcm
    