def solution(numbers, target):
    def dfs(depth, total):
        if depth == len(numbers):   # 맨 아래까지 탐색해서 타겟 넘버 만들어지면 1 반환
            return 1 if total == target else 0
        # + 붙이는 경우와 - 붙이는 경우의 수 각각 세서 더함
        return dfs(depth+1, total+numbers[depth]) + dfs(depth+1, total-numbers[depth])
    return dfs(0, 0)