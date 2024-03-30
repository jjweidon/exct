from collections import deque

N = int(input())
jido = [[int(x) for x in input()] for _ in range(N)]
visited= [[False if jido[j][i] else True for i in range(N)] for j in range(N)]
danji= []
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(j, i):
    q = deque([(j, i)])
    visited[j][i] = True
    cnt = 1
    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if ny in (-1, N) or nx in (-1, N) or visited[ny][nx]:
                continue
            q.append((ny, nx))
            visited[ny][nx] = True
            cnt += 1
    return cnt

for j in range(N):
    for i in range(N):
        if not visited[j][i]:
            danji.append(bfs(j, i))
danji.sort()

print(len(danji))
for x in danji:
    print(x)