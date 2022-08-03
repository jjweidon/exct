import sys
import math
input = sys.stdin.readline

W, H, X, Y, P = map(int, input().split())
cnt = 0

for _ in range(P):
    px, py = map(int, input().split())
    
    #W*H크기 직사각형 안에 있는 지
    if X <= px <= X+W and Y <= py <= Y+H:
        cnt += 1
    
    else:
        #플레이어와 (X,Y+H/2)의 거리가 H/2보다 작은지
        distance = math.sqrt(math.pow(px - X,2) + math.pow(py - (Y+H/2),2))
        if distance <= (H/2):
            cnt += 1
        else:
            #플레이어와 (X+W,Y+H/2)의 거리가 H/2보다 작은지
            distance = math.sqrt(math.pow(px - (X+W),2) + math.pow(py - (Y+H/2),2))
            if distance <= H/2:
                cnt += 1
print(cnt)