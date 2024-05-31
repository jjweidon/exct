N, M = map(int, input().split())
visited = [False] * (N+1)
stack = []

def dfs():
    if len(stack) == M:
        print(*stack)
        return
    
    for num in range(1, N+1):
        if visited[num]:
            continue
        stack.append(num)
        visited[num] = True
        dfs()
        stack.pop()
        visited[num] = False

dfs()
