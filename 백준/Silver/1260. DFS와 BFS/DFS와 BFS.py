from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = {i : [] for i in range(N+1)}

rs_dfs = [V]
rs_bfs = [V]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(N+1):
    graph[i].sort()

visited = [False for _ in range(N+1)]
visited[V] = True
def dfs(v):
    for next in graph[v]:
        if visited[next]:
            continue
        visited[next] = True
        rs_dfs.append(next)
        dfs(next)

def bfs(v):
    visited = [False for _ in range(N+1)]
    visited[V] = True
    q = deque([v])
    while q:
        cur = q.popleft()
        for next in graph[cur]:
            if visited[next]:
                continue
            q.append(next)
            visited[next] = True
            rs_bfs.append(next)

dfs(V)
bfs(V)

for e in rs_dfs:
    print(e, end=' ')
print()
for e in rs_bfs:
    print(e, end=' ')