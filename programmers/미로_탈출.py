from collections import deque

def solution(maps):
    H = len(maps)
    W = len(maps[0])
    answer = 0
    start = [0, 0]
    end = [0, 0]
    lever = [0, 0]
    
    # 시작점, 출구, 레버 찾기
    for j in range(H):
        for i in range(W):
            if maps[j][i] == 'S':
                start = [j, i]
            elif maps[j][i] == 'E':
                end = [j, i]
            elif maps[j][i] == 'L':
                lever = [j, i]
    
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    
    def check_time(s, e):
        step = 0
        visited = [[False] * W for _ in range(H)]
        q = deque([s])
        visited[s[0]][s[1]] = True
        while q:
            for _ in range(len(q)):
                ey, ex = q.popleft()
                if ey == e[0] and ex == e[1]:
                    return step
                for k in range(4):
                    ny = ey + dy[k]
                    nx = ex + dx[k]
                    if ny in (-1, H) or nx in (-1, W):
                        continue
                    if maps[ny][nx] == 'X' or visited[ny][nx] == True:
                        continue
                    q.append((ny, nx))
                    visited[ny][nx] = True
            step += 1
        return 0
    
    start_to_lever = check_time(start, lever)
    lever_to_end = check_time(lever, end)
    
    return start_to_lever + lever_to_end if start_to_lever and lever_to_end else -1