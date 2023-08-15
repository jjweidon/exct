N = int(input())
T, M = map(int, input().split())
for _ in range(N):
    c = int(input())
    T = (T + ((M + c) // 60)) % 24
    M = (M + c) % 60

print(T, M)