import sys
input = sys.stdin.readline
dwarfs = [int(input()) for _ in range(9)]
dwarfs.sort()
for d in dwarfs:
    for w in dwarfs:
        if sum(dwarfs) - d - w == 100:
            dwarfs.remove(d)
            dwarfs.remove(w)
            break
for dwarf in dwarfs:
    print(dwarf)