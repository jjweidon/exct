def solution(wallpaper):
    H = len(wallpaper)
    W = len(wallpaper[0])
    lux, luy, rdx, rdy = 0, 0, 0, 0

    btn = False
    for i in range(H):
        if "#" in wallpaper[i]:
            if not btn:
                lux = i
                btn = True
            rdx = i

    btn = False
    for j in range(W):
        for i in range(H):
            if wallpaper[i][j] == "#":
                if not btn:
                    luy = j
                    btn = True
                rdy = j

    answer = [lux, luy, rdx+1, rdy+1]
    return answer


# 정해 코드

def solution(wall):
    a, b = [], []
    for i in range(len(wall)):
        for j in range(len(wall[i])):
            if wall[i][j] == "#":
                a.append(i)
                b.append(j)
    return [min(a), min(b), max(a) + 1, max(b) + 1]