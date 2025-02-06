N, M = map(int, input().split())
brands = [tuple(map(int, input().split())) for _ in range(M)]
one = min(brands, key=lambda x: x[1])[1]
six = min(min(brands, key=lambda x: x[0])[0], one * 6)
rs = N // 6 * six + min(six, N % 6 * one)
print(rs)