# 나의 풀이

N = int(input())
T, M = map(int, input().split())
for _ in range(N):
    c = int(input())
    T = (T + ((M + c) // 60)) % 24
    M = (M + c) % 60

print(T, M)


# 정해 코드

N = int(input())
T, M = map(int, input().split())
c = [int(input()) for _ in range(N)]

time = (T * 60 + M + sum(c)) % 1440

hour = time // 60
minute = time % 60

print(hour, minute)