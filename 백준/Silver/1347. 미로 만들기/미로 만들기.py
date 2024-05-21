import sys
input = sys.stdin.readline
n = int(input())
st = input().strip()
maze = [['.']]
direction, i, j = 2, 0, 0
for s in st:
    if s == 'F':
        if direction == 0:
            i -= 1
        elif direction == 1:
            j += 1
        elif direction == 2:
            i += 1
        else:
            j -= 1
        if i < 0:
            maze.insert(0, ['#'] * len(maze[0]))
            i = 0
        if j >= len(maze[0]):
            for m in maze:
                m.append('#')
        if i >= len(maze):
            maze.append(['#'] * len(maze[0]))
        if j < 0:
            for m in maze:
                m.insert(0, '#')
            j = 0
        maze[i][j] = '.'
    elif s == 'L':
        direction = (direction + 3) % 4
    else:
        direction = (direction + 1) % 4
for m in maze:
    print(''.join(m))