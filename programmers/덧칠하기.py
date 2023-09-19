def solution(n, m, section):
    answer = 0
    wall = [False for _ in range(n+1)]
    for sect in section:
        wall[sect] = True
    
    i = 1
    while i <= n:
        if wall[i]:
            answer += 1
            i += m
        else:
            i += 1
    
    return answer


# 정해 코드

def solution(n, m, section):
    answer = 1
    prev = section[0]
    for sec in section:
        if sec - prev >= m:
            prev = sec
            answer += 1

    return answer