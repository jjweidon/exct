import sys; input = sys.stdin.readline

N, C = map(int, input().split())
houses = []
for _ in range(N):
    houses.append(int(input()))
houses.sort()

def binarySearch(result, C):
    start = 1
    end = houses[-1] - houses[0]

    while start <= end:
        mid = (start + end) // 2
        cnt = 1
        spot = houses[0]
        for i in range(1, len(houses)):
            if houses[i] >= spot + mid:
                spot = houses[i]
                cnt += 1
        
        if cnt >= C:
            start = mid + 1
            result = mid
        elif cnt < C:
            end = mid - 1
    result = end
    return result

result = 0
print(binarySearch(result, C))