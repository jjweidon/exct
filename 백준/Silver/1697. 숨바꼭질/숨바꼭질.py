from collections import deque

N, K = map(int, input().split())
time = [0 for _ in range(100001)] # visited
time[N] = 1
q = deque([N])

while q:
    cur = q.popleft()
    if cur == K:
        print(time[K]-1)
        break

    for next in (cur-1, cur+1, cur*2):
        if next < 0 or next > 100000 or time[next]:
            continue
        q.append(next)
        time[next] = time[cur] + 1