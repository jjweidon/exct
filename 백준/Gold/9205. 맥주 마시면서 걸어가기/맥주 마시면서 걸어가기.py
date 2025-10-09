from collections import deque
import heapq

def get_distance(ay, ax, by, bx):
    return abs(bx - ax) + abs(by - ay)

T = int(input())
for _ in range(T):
    n = int(input())
    sx, sy = map(int, input().split())
    ps = [tuple(map(int, input().split())) for _ in range(n)]
    visited = [False] * n
    ex, ey = map(int, input().split())
    
    q = deque([(sy, sx)])
    while q:
        cy, cx = q.popleft()
        if get_distance(cy, cx, ey, ex) <= 1000:
            print("happy")
            break
        for i, (px, py) in enumerate(ps):
            if visited[i]: continue
            if get_distance(cy, cx, py, px) > 1000: continue
            q.append((py, px))
            visited[i] = True
    else:
        print("sad")