import sys
input = sys.stdin.readline

n = int(input())
dices = [list(map(int, input().split())) for _ in range(n)]
opposite = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}
ans = [0] * 6

for i in range(6):
    dice = dices[0].copy()
    down = dice[i]
    up = dice[opposite[i]]
    dice.remove(down)
    dice.remove(up)
    ans[i] += max(dice)
    for j in range(1, n):
        dice = dices[j].copy()
        down = up
        up = dice[opposite[dice.index(down)]]
        dice.remove(down)
        dice.remove(up)
        ans[i] += max(dice)

print(max(ans))