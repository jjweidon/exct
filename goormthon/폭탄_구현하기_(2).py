N, K = map(int, input().split())
state = [[['',0] for _ in range(N)] for _ in range(N)]
for i in range(N):
    line = input().split()
    for j in range(N):
        state[i][j][0] = line[j]
bomb = [tuple(map(int, input().split())) for _ in range(K)]

for i in range(K):
    dy = [0, 1, -1, 0, 0]
    dx = [0, 0, 0, 1, -1]

    for j in range(5):
        y, x = bomb[i][0] - 1, bomb[i][1] - 1
        y += dy[j]
        x += dx[j]
        if y in (-1, N) or x in (-1, N):
            continue
        if state[y][x][0] == '0':
            state[y][x][1] += 1
        elif state[y][x][0] == '@':
            state[y][x][1] += 2

rs = 0
for i in range(N):
    rs = max(rs, max(state[i], key = lambda x: x[1])[1])

print(rs)