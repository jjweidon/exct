N, K = map(int, input().split())
M = [list(map(int, input().split())) for _ in range(N)]
visit = [[False] * N for _ in range(N)]
build = [0]  * 31

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
def bfs(j, i, building):
    q = [(j, i)]
    cnt = 1
    while q:
        ey, ex = q.pop()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0 <= ny < N and 0 <= nx < N:
                if not visit[ny][nx] and M[ny][nx] == building:
                    q.append((ny,nx))
                    cnt += 1
                    visit[ny][nx] = True

    if cnt >= K:
        return 1
    else:
        return 0

for j in range(N):
    for i in range(N):
        if not visit[j][i]:
            visit[j][i] = True
            build[M[j][i]] += bfs(j, i, M[j][i])

maxx = 0
rs = 30
for i in range(30, 0, -1):
    if build[i] > maxx:
        maxx = build[i]
        rs = i
print(rs)


# 정해 코드

# DFS

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(i, j):
	stack = [(i, j)]
	M = arr[i][j]
	cnt = 0

	while stack:
		y, x = stack.pop()

		if arr[y][x] != M:
			continue
		
		arr[y][x] = 0
		cnt += 1
		
		for k in range(4):
			ny, nx = y + dy[k], x + dx[k]
			
			if ny in (-1, N) or nx in (-1, N) or arr[ny][nx] != M:
				continue
			
			stack.append((ny, nx))
	
	return cnt

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
count = [0] * 31

for i in range(N):
	for j in range(N):
		if arr[i][j]:
			M = arr[i][j]
			if dfs(i, j) >= K:
				count[M] += 1

result, temp = 0, 0

for i in range(31):
	if temp <= count[i]:
		result = i
		temp = count[i]

print(result)

# BFS

from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(i, j):
	q = deque([(i, j)])
	M = arr[i][j]
	cnt = 0
	
	while q:
		y, x = q.popleft()
		
		if arr[y][x] != M:
			continue
		
		arr[y][x] = 0
		cnt += 1
		
		for k in range(4):
			ny, nx = y + dy[k], x + dx[k]
			
			if ny in (-1, N) or nx in (-1, N) or arr[ny][nx] != M:
				continue
			
			q.append((ny, nx))
	
	return cnt

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
count = [0] * 31

for i in range(N):
	for j in range(N):
		if arr[i][j]:
			M = arr[i][j]

			if bfs(i, j) >= K:
				count[M] += 1

result, temp = 0, 0

for i in range(31):
	if temp <= count[i]:
		result = i
		temp = count[i]

print(result)