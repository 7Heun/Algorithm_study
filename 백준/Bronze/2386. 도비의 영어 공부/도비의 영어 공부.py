while True:
    sen = input()
    if sen == '#':
        break
    c, s = sen.split(' ', 1)
    print(c, s.lower().count(c))