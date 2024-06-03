def print_star(n):
    if n == 1:
        return ['*']
    stars = print_star(n//3)
    arr = []
    for s in stars:
        arr.append(s*3)
    for s in stars:
        arr.append(s + ' '*(n//3) + s)
    for s in stars:
        arr.append(s*3)
    return arr

n = int(input())
print('\n'.join(print_star(n)))