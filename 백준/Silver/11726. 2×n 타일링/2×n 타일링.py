n = int(input())

tile = [1] * (n+1)

if n == 1:
    print(1)
else:
    for i in range(2, n+1):
        tile[i] = tile[i-1] + tile[i-2]
        if tile[i] >= 10007:
            tile[i] %= 10007
    print(tile[n])