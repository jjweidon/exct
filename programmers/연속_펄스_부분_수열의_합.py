def solution(sequence):
    N = len(sequence)
    
    case1 = []
    case2 = []
    for i, e in enumerate(sequence):
        if i % 2 == 0:
            case1.append(e)
            case2.append(-e)
        else:
            case1.append(-e)
            case2.append(e)
    
    dp1 = [0 for _ in range(N)]
    dp1[0] = case1[0]
    dp2 = [0 for _ in range(N)]
    dp2[0] = case2[0]

    for i in range(1, N):
        dp1[i] = max(dp1[i-1] + case1[i], case1[i])
        dp2[i] = max(dp2[i-1] + case2[i], case2[i])    

    return max(max(dp1), max(dp2))