def solution(n, l, r):
    answer = 0
    
    for i in range(l, r+1):
        num = i - 1
        while num > 0:
            rest = num % 5
            if rest == 2:
                break
            num //= 5
        else:
            answer += 1

    return answer