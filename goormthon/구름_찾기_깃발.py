N, K = map(int, input().split())
M = [list() for _ in range(N)]
for i in range(N):
    M[i] = list(map(int,input().split()))

def search(i, j):
    flag = 0
    if i != 0:
        if M[i-1][j] == 1: flag += 1
        if j != 0:
            if M[i-1][j-1] == 1: flag += 1
        if j != N-1:
            if M[i-1][j+1] == 1: flag += 1
    if i != N-1:
        if M[i+1][j] == 1: flag += 1
        if j != 0:
            if M[i+1][j-1] == 1: flag += 1
        if j != N-1:
            if M[i+1][j+1] == 1: flag += 1
    if j != 0:
        if M[i][j-1] == 1: flag += 1
    if j != N-1:
        if M[i][j+1] == 1: flag += 1

    return flag

result = 0
for i in range(N):
    for j in range(N):
        if M[i][j] == 1:
            continue
        flags = search(i, j)
        if flags == K:
            result += 1

print(result)