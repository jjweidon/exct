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