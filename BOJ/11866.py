from collections import deque

N, K = map(int, input().split())

que = deque()
que.extend([i + 1 for i in range(N)])

rs = []

for _ in range(N):
    for _ in range(K - 1):
        que.append(que.popleft())
    rs.append(que.popleft())

print("<", end="")
for i in range(N - 1):
    print(rs[i], end=", ")
print(f"{rs[N - 1]}>")