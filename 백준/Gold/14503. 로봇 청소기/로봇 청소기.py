dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N, M = map(int, input().split())
ey, ex, ed = map(int, input().split())
rooms = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

while True:
    if rooms[ey][ex] == 0:
        cnt += 1
    rooms[ey][ex] = 2

    for k in range(3, -1, -1):
        nd = (ed + k) % 4
        ny = ey + dy[nd]
        nx = ex + dx[nd]
        if rooms[ny][nx] != 0:
            continue
        ey, ex, ed = ny, nx, nd
        break
    
    else:
        ny = ey + dy[(ed + 2) % 4]
        nx = ex + dx[(ed + 2) % 4]
        if rooms[ny][nx] == 1:
            break
        ey, ex = ny, nx

print(cnt)