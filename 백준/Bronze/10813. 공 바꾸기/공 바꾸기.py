N, M = map(int, input().split())
changes = [tuple(map(int, input().split())) for _ in range(M)]
balls = [i+1 for i in range(N)]

for a, b in changes:
    balls[a-1], balls[b-1] = balls[b-1], balls[a-1]

print(*balls)