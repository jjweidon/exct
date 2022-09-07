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
            print(f'C1  start: {start}, end: {end}, mid: {mid}')
            return mid
        elif cnt < N:
            print(f'C2  start: {start}, end: {end}, mid: {mid}')
            end = mid - 1
        else:
            print(f'C3  start: {start}, end: {end}, mid: {mid}')
            start = mid + 1
    print(f'C4  start: {start}, end: {end}, mid: {mid}')
    return end

print(binarySearch(N))