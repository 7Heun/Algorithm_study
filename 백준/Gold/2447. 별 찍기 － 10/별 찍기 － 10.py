import sys
input = sys.stdin.readline

N = int(input())

def draw_star(n):
    if n == 1:
        return ['*']
    stars = draw_star(n // 3)
    arr = []

    # 위쪽 3등분 (***)
    for s in stars:
        arr.append(s * 3)
    # 중간쪽 3등분 (* *)
    for s in stars:
        arr.append(s + ' ' * (n // 3) + s)
    # 아래쪽 3등분 (***)
    for s in stars:
        arr.append(s * 3)
    
    return arr

print('\n'.join(draw_star(N)))
