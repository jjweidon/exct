import heapq

N = int(input())
M = int(input())
buses = [list(map(int, input().split())) for _ in range(M)]
start, end = map(int, input().split())
graph = [[] for _ in range(N+1)]
heap = []
distance = [float('inf')] * (N + 1)

for bus in buses:
    s, e, cost = bus
    graph[s].append((cost, e))

heapq.heappush(heap, (0, start))
distance[start] = 0

while heap:
    cw, cv = heapq.heappop(heap)
    if cw > distance[cv]:
        continue
    for nw, nv in graph[cv]:
        cost = cw + nw
        if cost < distance[nv]:
            distance[nv] = cost
            heapq.heappush(heap, (cost, nv))

print(distance[end])