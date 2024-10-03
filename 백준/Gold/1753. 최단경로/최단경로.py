import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
distance = [float('inf')] * (V+1)
heap = []

distance[K] = 0
heapq.heappush(heap, (0, K))

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

for i in range(1, V+1):
    if distance[i] == float('inf'):
        print('INF')
        continue
    print(distance[i])