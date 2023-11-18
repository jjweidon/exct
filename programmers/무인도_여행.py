import sys
sys.setrecursionlimit(10000)

def solution(maps):
    answer = []
    
    H = len(maps)
    W = len(maps[0])
    
    visited = [[False] * W for _ in range(H)]
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    
    def dfs(ey, ex):
        stamina = int(maps[ey][ex])
        visited[ey][ex] = True
        
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if not (0 <= ny < H and 0 <= nx < W):
                continue
            if not maps[ny][nx].isdecimal() or visited[ny][nx]:
                continue
            stamina += dfs(ny, nx)
        return stamina

    for j in range(H):
        for i in range(W):
            if not maps[j][i].isdecimal() or visited[j][i]:
                continue
            answer.append(dfs(j, i))
    
    answer = sorted(answer) if answer else [-1]
    return answer