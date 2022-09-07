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

    while start <= end:
        cnt = 0
        mid = (start + end) // 2
        for lan in lans:
            cnt += lan // mid
        
        if cnt == N:
            return mid
        elif cnt < N:
            end = mid - 1
        else:
            start = mid + 1
    return end

print(binarySearch(N))