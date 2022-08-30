N = int(input())
road = list(map(int, input().split()))
cost = list(map(int, input().split()))

lowest = cost[0]
result = lowest * road[0]

for i in range(1, N-1):
    if lowest > cost[i]:
        lowest = cost[i]

    result += lowest * road[i]

print(result)