N, L = map(int, input().split())
rs = []

for l in range(L, 101):
    if l % 2 == 1 and N % l == 0 and (N//l) - (l//2) >= 0:
        for i in range((N//l) - (l//2), (N//l) + (l//2) + 1):
            rs.append(i)
        break
    elif l % 2 == 0 and (N % l) * 2 == l and (N//l) - (l//2) + 1 >= 0:
        for i in range((N//l) - (l//2) + 1, (N//l) + (l//2) + 1):
            rs.append(i)
        break
else:
    rs.append(-1)

print(*rs)