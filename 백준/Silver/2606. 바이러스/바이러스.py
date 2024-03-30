from collections import deque

computer = int(input())
network = {com : [] for com in range(1, computer+1)}

pair = int(input())
for _ in range(pair):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

visited = [False for _ in range(computer+1)]
q = deque([1])
visited[1] = True
cnt = 0

while q:
    cur = q.popleft()
    cnt += 1
    for node in network[cur]:
        if visited[node]:
            continue
        q.append(node)
        visited[node] = True

print(cnt-1)