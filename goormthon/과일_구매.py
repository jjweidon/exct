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


# 정해 코드

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key=lambda x : x[1] // x[0])

result = 0

while K and arr:
	P, C = arr.pop()
	
	if K >= P:
		result += C
		K -= P
	else:
		result += C // P * K
		K = 0

print(result)