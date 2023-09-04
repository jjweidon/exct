N, M, K = map(int, input().split())
graph = {}
for i in range(M):
    s, e = map(int, input().split())
    graph[s] = graph.get(s, []) + [e]
    graph[e] = graph.get(e, []) + [s]
visit = [False] * (N + 1)

current = K
cnt = 1
while True:
    visit[current] = True
    nodes = graph.get(current, [])
    nodes.sort()
    for node in nodes:
        if not visit[node]:
            current = node
            cnt += 1
            break
    else:
        break

print(cnt, current)


# 정해 코드

# BFS
from collections import deque

def bfs(start):
	q = deque([start])
	
	while q:
		now = q.popleft()
		visited[now] = 1
		
		for to in sorted(graph[now]):
			if not visited[to]:
				q.append(to)
				break
		else:
			return now
	
N, M, K = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
	s, e = map(int, input().split())
	graph[s].append(e)
	graph[e].append(s)

result = bfs(K)
print(sum(visited), result)

# DFS

import sys
sys.setrecursionlimit(10**4)

def dfs(now):
	for to in sorted(graph[now]):
		if not visited[to]:
			visited[to] = 1
			return dfs(to)
	else:
		return now

N, M, K = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
	s, e = map(int, input().split())
	graph[s].append(e)
	graph[e].append(s)

visited[K] = 1
result = dfs(K)
print(sum(visited), result)