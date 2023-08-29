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