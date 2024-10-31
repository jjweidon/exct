import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    graph = [set() for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].add(b)
        graph[b].add(a)

    heap = [(0, 1)]
    visited = [False] * (N+1)
    airplane = 0

    while heap:
        cw, cv = heapq.heappop(heap)
        if visited[cv]:
            continue
        visited[cv] = True
        airplane += cw
        for nv in graph[cv]:
            if visited[nv]:
                continue
            heapq.heappush(heap, (1, nv))

    print(airplane)