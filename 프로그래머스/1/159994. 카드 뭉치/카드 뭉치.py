def solution(cards1, cards2, goal):
    if not goal:
        return "Yes"
    if cards1 and goal[0] == cards1[0]:
        return solution(cards1[1:], cards2, goal[1:])
    elif cards2 and goal[0] == cards2[0]:
        return solution(cards1, cards2[1:], goal[1:])
    else:
        return "No"