import sys; input = sys.stdin.readline

K, N = map(int, input().split())
lans = []
for _ in range(K):
    lan = int(input())
    lans.append(lan)
lans.sort()

def binarySearch(N):
    start = 1
    end = lans[-1]
    result = 0

    while start <= end:
        cnt = 0
        mid = (start + end) // 2
        for lan in lans:
            cnt += lan // mid
        
        if cnt >= N:
            start = mid + 1
        else:
            end = mid - 1
    result = end
    return result

print(binarySearch(N))