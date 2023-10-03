def solution(order):
    answer = 0
    
    conveyor = [i for i in range(len(order), 0, -1)]
    bozo = []
    
    for i, od in enumerate(order):
        if bozo and bozo[-1] == od:
            bozo.pop()
            answer += 1
            continue
        
        if not conveyor:
            break
        
        while conveyor:
            box = conveyor.pop()
            if box == od:
                answer += 1
                break
            else:
                bozo.append(box)
    
    return answer


# 정해 코드

def solution(order):
    stacks = []
    N = len(order)
    i = 1
    idx = 0
    while i < N+1:
        stacks.append(i)
        while stacks[-1] == order[idx]:
            idx += 1
            stacks.pop()
            if len(stacks) == 0:
                break
        i += 1

    return idx