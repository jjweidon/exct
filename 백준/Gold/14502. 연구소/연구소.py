import itertools
from collections import deque
import copy

N, M = map(int, input().split())
jido = [list(map(int, input().split())) for _ in range(N)]
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
blank = []

for j in range(N):
    for i in range(M):
        if jido[j][i]:
            continue
        blank.append((j, i))
make = list(itertools.combinations(blank, 3))

def bfs():
    maps = copy.deepcopy(jido)
    visited = [[True if jido[j][i] == 1 else False for i in range(M)] for j in range(N)]
    for j in range(N):
        for i in range(M):
            if visited[j][i] or not maps[j][i]:
                continue
            q = deque([(j, i)])
            visited[j][i] = True
            while q:
                ey, ex = q.popleft()
                for k in range(4):
                    ny = ey + dy[k]
                    nx = ex + dx[k]
                    if ny in (-1, N) or nx in (-1, M) or visited[ny][nx]:
                        continue
                    maps[ny][nx] = 2
                    visited[ny][nx] = True
                    q.append((ny, nx))
    
    # 안전지역 카운트
    cnt = 0
    for j in range(N):
        for i in range(M):
            if maps[j][i]:
                continue
            cnt += 1
    return cnt

maxx = 0
for case in make:
    for c in case:
        jido[c[0]][c[1]] = 1
    temp = bfs()
    maxx = max(maxx, temp)
    for c in case:
        jido[c[0]][c[1]] = 0
print(maxx)