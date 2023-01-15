n = int(input())

tile = [0] * (n+1)

tile[1] = 1
if n != 1:
    tile[2] = 3
    for i in range(3, n+1):
        tile[i] = tile[i-1] + (tile[i-2] * 2)
        if tile[i] >= 10007:
            tile[i] %= 10007

print(tile[n])