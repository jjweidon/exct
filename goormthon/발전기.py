import sys
input = sys.stdin.readline

N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]
visit = [[False] * N for _ in range(N)]
power = 0

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
def bfs(j, i):
    q = [(j, i)]
    while q:
        ey, ex = q.pop()
        for d in range(4):
            ny = ey + dy[d]
            nx = ex + dx[d]
            if 0 <= ny < N and 0 <= nx < N:
                if M[ny][nx] == 1 and visit[ny][nx] == False:
                    q.append((ny, nx))
                    visit[ny][nx] = True

for j in range(N):
    for i in range(N):
        if M[j][i] == 1 and visit[j][i] == False:
            bfs(j, i)
            power += 1

print(power)


# 정해 코드

# DFS (비재귀)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 0

def dfs(i, j):
	stack = [(i, j)]
	
	while stack:
		y, x = stack.pop()
		
		if not arr[y][x]:
			continue
		
		arr[y][x] = 0
		
		for k in range(4):
			ny, nx = y + dy[k], x + dx[k]
			
			if ny in (-1, N) or nx in (-1, N) or not arr[ny][nx]:
				continue
			
			stack.append((ny, nx))

for i in range(N):
	for j in range(N):
		if arr[i][j]:
			result += 1
			dfs(i, j)

print(result)

# BFS

from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 0

def bfs(i, j):
	q = deque([(i, j)])
	
	while q:
		y, x = q.popleft()
		
		if not arr[y][x]:
			continue
		
		arr[y][x] = 0
		
		for k in range(4):
			ny, nx = y + dy[k], x + dx[k]
			
			if ny in (-1, N) or nx in (-1, N) or not arr[ny][nx]:
				continue
			
			q.append((ny, nx))
			
for i in range(N):
	for j in range(N):
		if arr[i][j]:
			result += 1
			bfs(i, j)

print(result)