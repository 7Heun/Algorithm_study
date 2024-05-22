import sys
input = sys.stdin.readline
dwarfs = [int(input()) for _ in range(9)]
dwarfs.sort()
total = sum(dwarfs)
def find_dwarfs(dwarfs, total):
    for d in dwarfs:
        for w in dwarfs:
            if d != w and total - d - w == 100:
                dwarfs.remove(d)
                dwarfs.remove(w)
                return dwarfs
dwarfs = find_dwarfs(dwarfs, total)
for dwarf in dwarfs:
    print(dwarf)