import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(cur):
    global turn
    visit[cur] = turn
    turn += 1
    for node in sorted(nodes[cur]):
        if not visit[node]:
            dfs(node)

N, M, R = map(int, input().split())
nodes = [[] for _ in range(N+1)]
visit = [0] * (N+1)
for _ in range(M):
    u, v = map(int, input().split())
    nodes[u].append(v)
    nodes[v].append(u)

turn = 1
dfs(R)

for rs in visit[1:]:
    print(rs)