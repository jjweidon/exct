N, K = map(int, input().split())
fruits = [[0, 0] for _ in range(N)]
for i in range(N):
    fruits[i][0], fruits[i][1] = map(int, input().split())
    fruits[i][1] //= fruits[i][0]

rs = 0
fruits.sort(key = lambda x: -x[1])

for fruit in fruits:
    if fruit[0] <= K:
        rs += fruit[0] * fruit[1]
    else:
        rs += K * fruit[1]
    K -= fruit[0]
    if K <= 0:
        break

print(rs)