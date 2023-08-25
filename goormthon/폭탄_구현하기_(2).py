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


# 정해 코드

N, K = map(int, input().split())
arr = [list(input().split()) for _ in range(N)]
score = [[0] * N for _ in range(N)]

dy = [0, 1, -1, 0, 0]
dx = [0, 0, 0, 1, -1]

for _ in range(K):
	y, x = map(int, input().split())
	y -= 1
	x -= 1
	
	for k in range(5):
		ny = y + dy[k]
		nx = x + dx[k]
		
		if ny < 0 or ny >= N or nx < 0 or nx >= N or arr[ny][nx] == "#":
			continue
		
		if arr[ny][nx] == "@":
			score[ny][nx] += 2
		else:
			score[ny][nx] += 1

result = 0

# for i in range(N):
# 	for j in range(N):
# 		result = max(result, score[i][j])

result = max([max(i) for i in score])

print(result)