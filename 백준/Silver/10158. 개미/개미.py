w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

np = (t - (w - p)) % w if ((t - (w - p)) // w) % 2 == 1 else w - ((t - (w - p)) % w)
nq = (t - (h - q)) % h if ((t - (h - q)) // h) % 2 == 1 else h - ((t - (h - q)) % h)

print(np, nq)