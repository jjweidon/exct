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
    com_cnt, line_cnt = 0, 0
    coms = []
    q = deque([computer])
    while q:
        current = q.pop()
        if not visited[current]:
            coms.append(current)
            visited[current] = True
            com_cnt += 1
            for next in graph[current]:
                if not visited[next]:
                    line_cnt += 1
                    graph[next].remove(current)
                    q.append(next)
    
    coms.sort()
    return coms, com_cnt, line_cnt

for computer in range(1, N+1):
    if not graph[computer] or visited[computer]:
        continue
    components.append(bfs(computer))

components.sort(key=lambda x: (-x[2]/x[1], x[1], x[0][0]))

for num in components[0][0]:
    print(num, end=' ')