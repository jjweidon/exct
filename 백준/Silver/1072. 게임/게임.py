import math

X, Y = map(int, input().split())
Z = Y * 100 // X
k = ((Z * X) + X - (100 * Y)) / (99 - Z) if Z < 99 else -1

print(math.ceil(k))