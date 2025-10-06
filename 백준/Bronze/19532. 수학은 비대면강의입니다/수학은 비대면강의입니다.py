a, b, c, d, e, f = map(int, input().split())
x = (b * f - e * c) // (b * d - e * a)
y = (a * f - d * c) // (e * a - b * d)
print(x, y)
