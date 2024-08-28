
dy = [1, -1, 0 ,0]
dx = [0, 0, 1, -1]

T = int(input())
for _ in range(T):

    n = int(input())
    sticker = [[], []]
    sticker[0] = list(map(int, input().split()))
    sticker[1] = list(map(int, input().split()))
    maxx = [[0] * n for _ in range(2)]

    maxx[0][0] = sticker[0][0]
    maxx[1][0] = sticker[1][0]
    if n > 1:
        maxx[0][1] = maxx[1][0] + sticker[0][1]
        maxx[1][1] = maxx[0][0] + sticker[1][1]
    
    for i in range(2, n):
        maxx[0][i] = sticker[0][i] + max(maxx[1][i-2], maxx[1][i-1])
        maxx[1][i] = sticker[1][i] + max(maxx[0][i-2], maxx[0][i-1])
    
    print(max(maxx[0][-1], maxx[1][-1]))