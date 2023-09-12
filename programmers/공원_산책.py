def solution(park, routes):
    answer = []
    H = len(park)
    W = len(park[0])
    ey, ex = 0, 0

    for j in range(H):
        if "S" in park[j]:
            for i in range(W):
                if park[j][i] == "S":
                    ey, ex = j, i
                    break
            break

    for route in routes:
        ny, nx = ey, ex
        op, n = route.split()
        n = int(n)
        if op == "E":
            nx = ex + n
        if op == "N":
            ny = ey - n
        if op == "S":
            ny = ey + n
        if op == "W":
            nx = ex - n
        
        print(ey, ex, ny, nx)
        
        if H <= ny or ny < 0 or W <= nx or nx < 0:
            ny, nx = ey, ex
            continue
        
        btn = False
        for j in range(min(ey, ny), max(ey, ny) + 1):
            if "X" in park[j]:
                for i in range(min(ex, nx), max(ex, nx) + 1):
                    if park[j][i] == "X":
                        ny, nx = ey, ex
                        btn = True
                        break
            if btn:
                break
        ey, ex = ny, nx

    answer.append(ny)
    answer.append(nx)
    return answer

park = ["OXO","OOX","OXO","OOS"]
# routes = ["E 2","N 1","W 1", "N 1", "W 2", "N 1"]
routes = ["N 3"]

print(solution(park, routes))