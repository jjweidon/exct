def solution(scores):
    wanho = scores[0]    
    scores.sort(key=lambda x: (-x[0], -x[1]))
    insentive = [scores[0]]
    limit_x, limit_y = scores[0][0], scores[0][1]
    temp_x, temp_y = limit_x, limit_y

    for i in range(1, len(scores)):      
        x, y = scores[i][0], scores[i][1]
        if x < temp_x:
            limit_x = temp_x
            limit_y = temp_y
            temp_x = x
            if y > limit_y:
                temp_y = y
        
        if x < limit_x and y < limit_y:
            continue
        insentive.append(scores[i])
        
    insentive.sort(key=lambda x: -(x[0]+x[1]))
    
    rank = 1
    maxx = sum(insentive[0])
    for i in range(len(insentive)):
        if sum(insentive[i]) < maxx:
            maxx = sum(insentive[i])
            rank = i+1        
        if insentive[i] == wanho:
            return rank
    return -1