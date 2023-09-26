def distance(x1, y1, x2, y2):
    return (x1 - x2)**2 + (y1 - y2)**2

def solution(m, n, startX, startY, balls):
    answer = []
    
    for i, ball in enumerate(balls):
        endX, endY = ball
        
        min_dist = float("inf")

        cases = [(-endX, endY), (2*m -endX, endY), (endX, -endY), (endX, 2*n - endY)]
        for i, case in enumerate(cases):
            modX, modY = case[0], case[1]

            # 벽에 부딪히기 전에 공에 맞는 경우
            if startY == endY:
                if i == 0 and startX > endX:
                    continue
                if i == 1 and startX < endX:
                    continue
            if startX == endX:
                if i == 2 and startY > endY:
                    continue
                if i == 3 and startY < endY:
                    continue
            
            # 대칭 좌표와의 거리
            min_dist = min(min_dist, distance(startX, startY, modX, modY))

        answer.append(round(min_dist))
        
    return answer


# 정해 코드

def solution(m, n, startX, startY, balls):
    answer = []
    targets=[(-startX,startY),(startX,2*n-startY),(2*m-startX,startY),(startX,-startY)]
    for ball in balls:
        new_targets=[targets[0],targets[1],targets[2],targets[3]]
        if startX==ball[0]:
            new_targets=[targets[0],targets[1],targets[2]] if startY>ball[1] else [targets[0],targets[3],targets[2]]
        if startY==ball[1]:
            new_targets=[targets[1],targets[2],targets[3]] if startX>ball[0] else [targets[0],targets[1],targets[3]]
        answer.append(min(list(map(lambda target:(ball[0]-target[0])**2+(ball[1]-target[1])**2,new_targets))))
    return answer