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