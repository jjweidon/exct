N = int(input())
matrix = [list(map(str, input())) for _ in range(N)]
friends1 = [set() for _ in range(N)]
friends2 = [set() for _ in range(N)]
cnt = [0] * (N)

# 1 친구 구하기
for i in range(N):
    for j in range(i+1, N):
        if matrix[i][j] == "N":
            continue
        friends1[i].add(j)
        friends1[j].add(i)

# 2 친구 구하기
for i in range(N):
    for depth1 in friends1[i]:
        for depth2 in friends1[depth1]:
            if depth2 == i:
                continue
            friends2[i].add(depth2)

# 1 친구 | 2 친구 (합집합)
for i in range(N):
    friends1[i] |= friends2[i]

print(len(max(friends1, key=lambda x: len(x))))