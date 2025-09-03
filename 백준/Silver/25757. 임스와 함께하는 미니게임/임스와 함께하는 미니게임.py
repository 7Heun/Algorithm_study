import sys
input = sys.stdin.readline

games = {'Y': 1, 'F': 2, 'O': 3}
n, g = input().strip().split()
players = set()
for _ in range(int(n)):
    players.add(input().rstrip())
print(len(players) // games[g])