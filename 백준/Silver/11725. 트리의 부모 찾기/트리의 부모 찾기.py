from collections import deque

N = int(input())
n = [map(int, input().split()) for _ in range(N-1)]
tree = dict()
for n1, n2 in n:
    tree[n1] = tree.get(n1, [])
    tree[n1].append(n2)
    tree[n2] = tree.get(n2, [])
    tree[n2].append(n1)

parent = [0] * (N+1)
visited = [False] * (N+1)
q = deque([1])
while q:
    node = q.popleft()
    visited[node] = True
    for child in tree[node]:
        if visited[child]:
            continue
        q.append(child)
        parent[child] = node

for i in range(2, N+1):
    print(parent[i])