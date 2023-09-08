import sys
from collections import deque
input = sys.stdin.readline

N, M, S, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
rs = [0 for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(gongsa):
    visited = [False for _ in range(N+1)]
    distance = [0 for _ in range(N+1)]
    q = deque([S])
    distance[S] = 1
    while q:
        current = q.popleft()
        visited[current] = True
        if current == E:
            return distance[E]
        
        for next in graph[current]:
            if next != gongsa and not visited[next]:
                q.append(next)
                distance[next] = distance[current] + 1 if not distance[next] else distance[next]
    
    return -1

for day in range(1, N+1):
    rs[day] = bfs(day) if (not day in (S, E)) else -1

for i in range(1,N+1):
    print(rs[i])


# 정해 코드

from collections import deque

def bfs(start, off):
	if start == off:
		return -1
	
	visited = [0] * (N + 1)
	q = deque([start])
	visited[start] = 1
	step = 1
	
	while q:
		step += 1
		for _ in range(len(q)):
			now = q.popleft()

			for to in graph[now]:
				if visited[to] or to == off:
					continue
					
				if to == E:
					return step
				
				visited[to] = 1
				q.append(to)
	
	return -1
	
N, M, S, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
	u, v = map(int, input().split())
	graph[u].append(v)
	graph[v].append(u)

for i in range(1, N + 1):
	print(bfs(S, i))