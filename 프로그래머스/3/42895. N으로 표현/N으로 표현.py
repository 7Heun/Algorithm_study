def solution(N, number):
    if N == number:
        return 1
    dp = [set() for _ in range(9)]
    
    for i in range(1, 9):
        # 같은 숫자 반복으로 만들 수 있는 수
        dp[i].add(int(str(N)*i))
        # dp[j], dp[i-j]로 가능한 조합
        for j in range(1, i):
            for num1 in dp[j]:
                for num2 in dp[i-j]:
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)
                    if num2 != 0: dp[i].add(num1 // num2)
        if number in dp[i]: return i
    return -1