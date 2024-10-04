import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append((1,B))
heap = []
distance = [INF] * (N+1)

heapq.heappush(heap, (0, X))
distance[X] = 0

while heap:
    cw, cv = heapq.heappop(heap)
    if cw > distance[cv]:
        continue
    for nw, nv in graph[cv]:
        cost = cw + nw
        if cost >= distance[nv]:
            continue
        heapq.heappush(heap, (cost, nv))
        distance[nv] = cost

check = False
for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        check = True
if not check:
    print(-1)