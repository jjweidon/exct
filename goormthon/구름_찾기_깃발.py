N, K = map(int, input().split())
M = [list() for _ in range(N)]
for i in range(N):
    M[i] = list(map(int,input().split()))

def search(i, j):
    flag = 0
    if i != 0:
        if M[i-1][j] == 1: flag += 1
        if j != 0:
            if M[i-1][j-1] == 1: flag += 1
        if j != N-1:
            if M[i-1][j+1] == 1: flag += 1
    if i != N-1:
        if M[i+1][j] == 1: flag += 1
        if j != 0:
            if M[i+1][j-1] == 1: flag += 1
        if j != N-1:
            if M[i+1][j+1] == 1: flag += 1
    if j != 0:
        if M[i][j-1] == 1: flag += 1
    if j != N-1:
        if M[i][j+1] == 1: flag += 1

    return flag

result = 0
for i in range(N):
    for j in range(N):
        if M[i][j] == 1:
            continue
        flags = search(i, j)
        if flags == K:
            result += 1

print(result)


# 정해 코드

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]

N, K = map(int, input().split())

# matrix = []

# for _ in range(N):
# 	row = list(input().split())
# 	matrix.append(row)

matrix = [list(input().split()) for _ in range(N)]

result = 0

for i in range(N):
	for j in range(N):
		if matrix[i][j] == "1":
			continue
		
		check = 0
		
		for k in range(8):
			y = i + dy[k]
			x = j + dx[k]

			if y < 0 or y >= N or x < 0 or x >= N:
				continue
			
			if matrix[y][x] == "1":
				check += 1

		if check == K:
			result += 1

print(result)