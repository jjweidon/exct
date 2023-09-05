import sys
input = sys.stdin.readline

N, M = map(int, input().split())
island = [[] for _ in range(N+1)]
visit = [False for _ in range(N+1)]
cnt = 0

for i in range(M):
    s, e = map(int, input().split())
    island[s].append(e)

def dfs(i):
    stack = [i]
    while stack:
        current = stack.pop()
        visit[current] = True
        for next in island[current]:
            if not visit[next] and current in island[next]:
                stack.append(next)
    return 1

for i in range(1, N+1):
    if not visit[i]:
        cnt += dfs(i)

print(cnt)


# 정해 코드

from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
result = 0

for _ in range(M):
	s, e = map(int, input().split())
	graph[s].append(e)

for i in range(1, N + 1):
	if visited[i]:
		continue
	
	q = deque([i])
	result += 1
	visited[i] = 1
	
	while q:
		now = q.popleft()
		for to in graph[now]:
			if not visited[to] and now in graph[to]:
				q.append(to)
				visited[to] = 1
	
print(result)