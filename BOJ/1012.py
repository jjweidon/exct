import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    def dfs(j, i):
        stack = [(j, i)]
        while stack:
            ey, ex = stack.pop()
            visit[ey][ex] = True
            for k in range(4):
                ny = ey + dy[k]
                nx = ex + dx[k]
                if 0 <= ny < N and 0 <= nx < M:
                    if cabbage[ny][nx] and not visit[ny][nx]:
                        stack.append((ny, nx))
        
        return 1

    M, N, K = map(int, input().split())
    cabbage = [[0] * M for _ in range(N)]
    visit = [[False] * M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        cabbage[Y][X] = 1
    rs = 0
    
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    for j in range(N):
        for i in range(M):
            if cabbage[j][i] and not visit[j][i]:
                rs += dfs(j, i)
    
    print(rs)