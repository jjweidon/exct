import math
import sys
input = sys.stdin.readline

T = int(input()) #테스트케이스
cnt = []

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split()) #출발점과 도착점
    n = int(input()) #행성의 개수
    temp = 0 #각 케이스의 result
    for _ in range(n):
        cx, cy, r = map(int, input().split()) #행성의 중점과 반지름
        distStart = math.sqrt(math.pow(cx-x1,2)+math.pow(cy-y1,2)) #출발점과 행성 중심 간의 거리
        distEnd = math.sqrt(math.pow(cx-x2,2)+math.pow(cy-y2,2)) #도착점과 행성 중심 간의 거리
        ###두점 사이의 거리 성능 비교하기###
        
        #행성계의 경계를 기준으로 출발점과 도착점이 분리되어 있으면 카운트
        if (distStart < r and distEnd > r) or (distStart > r and distEnd < r):
            temp += 1
    cnt.append(temp)

for x in cnt:
    print(x)