from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edge = [list(map(int, input().split())) for _ in range(M)]
graph = [[] for _ in range(N+1)]
for u, v in edge:
    graph[u].append(v)
    graph[v].append(u)
cnt = 0
visitied = [False] * (N+1)

def bfs(n):
    q = deque([n])
    visitied[n] = True
    while(q):
        currtent = q.popleft()
        for next in graph[currtent]:
            if visitied[next]:
                continue
            q.append(next)
            visitied[next] = True
    return 1

for i in range(1, N+1):
    if visitied[i]:
        continue
    cnt += bfs(i)

print(cnt)