from collections import deque

def solution(game_board, table):
    # 이어진 블럭 찾는 dfs 함수
    def dfs(x, y, base_x, base_y, target_value, board, visited):
        block = []
        visited[x][y] = True
        stack = deque([(x, y)])
        while stack:
            cx, cy = stack.pop()
            block.append((cx - base_x, cy - base_y))
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < len(board) and 0 <= ny < len(board) and not visited[nx][ny]:
                    if board[nx][ny] == target_value:
                        visited[nx][ny] = True
                        stack.append((nx, ny))
        return block
    
    # 블럭 90도 회전시키는 함수
    def rotate(block):
        return [(-y, x) for x, y in block]
    # 블럭 모양 표준화하는 함수 (x, y 최솟값을 기준으로 좌표가 0, 0부터 시작하게 조정)
    def normalize(block):
        min_x, min_y = min(x for x, y in block), min(y for x, y in block)
        return sorted([(x - min_x, y - min_y) for x, y in block])
    
    N = len(table)
    ans = 0
    
    # table에서 1로 이어진 블럭들 추출해서 저장
    visited = [[False] * N for _ in range(N)]
    blocks = []
    for i in range(N):
        for j in range(N):
            if table[i][j] == 1 and not visited[i][j]:
                block = dfs(i, j, i, j, 1, table, visited)
                blocks.append(normalize(block))
    
    # game_board에서 0으로 이어진 빈 공간 추출해서 맞는 블럭 있는지 확인
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if game_board[i][j] == 0 and not visited[i][j]:
                vacancy = dfs(i, j, i, j, 0, game_board, visited)
                matched = False
                for block in blocks:
                    rotated = block[:]
                    for _ in range(4):
                        rotated = rotate(rotated)
                        if normalize(rotated) == normalize(vacancy):
                            ans += len(rotated)
                            blocks.remove(block)
                            matched = True
                            break
                    if matched: break
    return ans