'''
key의 1 부분과 lock의 0 부분이 정확히 일치하도록 => 배열끼리 겹쳐서 합했을 때 0이나 2가 없어야 함
key를 회전 및 이동 => rotate()
check()
열 수 있으면 true, 아니면 false
브루트포스?
'''

def rotate(arr):
    return list(map(list, zip(*arr[::-1])))

def check(board, M, N):
    # 자물쇠 영역(가운데 N*N)이 모두 1인지 확인
    for i in range(N):
        for j in range(N):
            if board[M+i][M+j] != 1: return False
    return True
    
def solution(key, lock):
    M = len(key)
    N = len(lock)
    
    # 보드 확장
    board_size = M * 2 + N
    board = [[0] * board_size for _ in range(board_size)]
    
    # 자물쇠를 보드 정중앙에 배치
    for i in range(N):
        for j in range(N):
            board[M+i][M+j] = lock[i][j]
    
    # 4방향 탐색
    for _ in range(4):
        key = rotate(key) # key 90도 회전
        
        # key를 board 위에서 이동하면서 일치하는지 확인
        for x in range(1, board_size - M):
            for y in range(1, board_size - M):
                # 도화지 위에 열쇠 더하기 (i, j는 열쇠 내부의 인덱스)
                for i in range(M):
                    for j in range(M):
                        board[x + i][y + j] += key[i][j]
                
                # 맞물리는지 확인
                if check(board, M, N):
                    return True
                
                # 맞지 않다면 board 원상복구
                for i in range(M):
                    for j in range(M):
                        board[x + i][y + j] -= key[i][j]

    return False