import sys
input = sys.stdin.readline

from collections import deque

M, N = map(int, input().split())
tomatos = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
q = deque([])

# 초기 1 찾기
for j in range(N):
    for i in range(M):
        if tomatos[j][i] in (1, -1):
            visited[j][i] = True
            if tomatos[j][i] == 1:
                q.append((j, i))

if not q:
    print(0)

else:
    answer = -1
    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]

    while q:
        temp = q.copy()
        q.clear()
        while temp:
            ey, ex = temp.popleft()
            for k in range(4):
                ny = ey + dy[k]
                nx = ex + dx[k]
                if ny in (-1, N) or nx in (-1, M):
                    continue
                if visited[ny][nx] == True:
                    continue
                visited[ny][nx] = True
                q.append((ny, nx))
        answer += 1
    
    for j in range(N):
        if False in visited[j]:
            print(-1)
            break
    else:
        print(answer)