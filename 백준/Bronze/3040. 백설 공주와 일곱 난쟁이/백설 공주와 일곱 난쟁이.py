import sys
input = sys.stdin.readline
dwarfs = [int(input()) for _ in range(9)]
total = sum(dwarfs)
dwarfs.sort()
for d in dwarfs:
    for e in dwarfs:
        if d != e and total - d - e == 100:
            dwarfs.remove(d)
            dwarfs.remove(e)
            break
for dwarf in dwarfs:
    print(dwarf)