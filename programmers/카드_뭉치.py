from collections import deque

def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)
    answer = "Yes"
    
    while goal:
        if cards1 and cards1[0] == goal[0]:
            cards1.popleft()
        elif cards2 and cards2[0] == goal[0]:
            cards2.popleft()
        else:
            answer = "No"
            break
        goal.popleft()
    
    return answer

# 정해 코드

def solution(cards1, cards2, goal):
    for g in goal:
        if len(cards1) > 0 and g == cards1[0]:
            cards1.pop(0)       
        elif len(cards2) > 0 and g == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"