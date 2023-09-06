import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
components = []
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(computer):
    line_cnt = 0
    coms = set()
    q = deque([computer])
    while q:
        current = q.pop()
        coms.add(current)
        visited[current] = True
        for next in graph[current]:
            if not visited[next]:
                line_cnt += 1
                graph[next].remove(current)
                q.append(next)
    
    coms = list(coms)
    coms.sort()
    return coms, len(coms), line_cnt

for computer in range(1, N+1):
    if not graph[computer] or visited[computer]:
        continue
    components.append(bfs(computer))

components.sort(key=lambda x: (-x[2]/x[1], x[1], x[0][0]))

for num in components[0][0]:
    print(num, end=' ')


# 정해 코드

from collections import deque

def bfs(start):
	q = deque([start])
	component = set()
	
	while q:
		now = q.popleft()
		
		if visited[now]:
			continue
		
		visited[now] = 1
		component.add(now)
		
		for to in graph[now]:
			if not visited[to]:
				q.append(to)
	
	edge = 0
	
	for i in component:
		for to in graph[i]:
			if to in component:
				edge += 1
	
	return sorted(list(component)), edge / len(component) 

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

result, density = [], 0

for i in range(1, N + 1):
	if not visited[i]:
		temp, tempDensity = bfs(i)
		
		if abs(tempDensity - density) < 1e-8:
			if len(result) > len(temp):
				result = temp
				density = tempDensity
			elif len(result) == len(temp):
				if temp[0] < result[0]:
					result = temp
					density = tempDensity
		elif tempDensity > density:
			result = temp
			density = tempDensity

print(*result)