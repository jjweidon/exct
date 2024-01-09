def solution(scores):
    wanho = scores[0]    
    scores.sort(key=lambda x: (-x[0], -x[1]))
    insentive = [scores[0]]
    limit_x, limit_y = scores[0][0], scores[0][1]
    for i in range(1, len(scores)):
        x, y = scores[i][0], scores[i][1]
        if x < limit_x and y < limit_y:
            continue
        if y > limit_y:
            limit_y = y
        if x < limit_x:
            limit_x = insentive[-1][0]
        insentive.append(scores[i])
    
    insentive.sort(key=lambda x: -(x[0]+x[1]))
    
    rank = 1
    maxx = insentive[0][0] + insentive[0][1]
    for i in range(len(insentive)):
        if insentive[i][0] + insentive[i][1] < maxx:
            maxx = insentive[i][0] + insentive[i][1]
            rank = i+1        
        if insentive[i] == wanho:
            return rank
    return -1