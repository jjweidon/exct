import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coin = []
for _ in range(N):
    coin.append(int(input()))
coin.sort(reverse=True) # 동전 가치 내림차순으로 정렬

result = 0
for i in range(N):
    result += K // coin[i]
    K %= coin[i]

print(result)
